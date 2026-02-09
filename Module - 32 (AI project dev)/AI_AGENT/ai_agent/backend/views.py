import json
import uuid
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests

from ai_agent.settings import OPENROUTER_API_KEY
from backend.models import ChatMessage

# Create your views here.
def chat_view(request):
    session_id = request.session.get('chat_session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        request.session['chat_session_id'] = session_id
    messages = ChatMessage.objects.filter(session_id=session_id)
    
    context = {
        'messages': messages,
        'session_id': session_id
    }
    return render(request, 'chat.html', context)

@csrf_exempt 
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message').strip()
            session_id = request.session.get('session_id', str(uuid.uuid4()))
            
            if not user_message:
                return JsonResponse({'error': 'Empty message'}, status=400)
            
            if len(user_message) > 5000:
                user_message = user_message[:5000]
            
            #save user message to db
            ChatMessage.objects.create(
                session_id=session_id,
                role='user',
                message=user_message
            )
            
            #get conversation history   
            history = ChatMessage.objects.filter(session_id=session_id).order_by('timestamp')
            
            #build messages for api
            api_messages = [
                {
                    "role": "system",
                    "content": """You are a helpful and friendly ecommerce assistant. You help the customers with:
                    - Product inquiries recommendations
                    - Order tracking and status updates
                    - Return and refund policies
                    - SHipping information and delivery times
                    - Payment options and issues
                    - General product information and support
                    
                    Be professional and courteous in your responses. If you don't know the answer, say you don't know but offer to help with something else. Always try to assist the customer to the best of your ability.
                    """
                }
            ]
            #add conversation history to messages
            for msg in history:
                api_messages.append({
                    "role": msg.role,
                    "content": msg.message
                })
            
            #call openrouter api
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek/deepseek-r1-0528:free",  # Free open source model
                    "messages": api_messages,
                    "temperature": 0.7,
                    "max_tokens": 2000,  # Increased for better responses
                }
            )
            if response.status_code == 200:
                ai_response = response.json()
                assistant_message = ai_response['choices'][0]['message']['content']
                #limit assistant message to 5000 characters
                if len(assistant_message) > 5000:
                    assistant_message = assistant_message[:5000]+"..."
            #save assistant message to db
                ChatMessage.objects.create(
                    session_id=session_id,
                    role='assistant',
                    message=assistant_message
                )
                return JsonResponse({
                    'success': True,
                    'message': assistant_message,
                    'session_id': session_id})
            else:
                return JsonResponse({'error': 'Failed to get response from AI'}, status=500)
            
            return JsonResponse({'message': assistant_message})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def clear_chat(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = data.get('session_id')
            if session_id:
                ChatMessage.objects.filter(session_id=session_id).delete()
                return JsonResponse({'success': True, 'message': 'Chat cleared'})
            return JsonResponse({'error': 'Session ID not provided'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)