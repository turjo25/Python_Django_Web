from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,filters
from .models import Author,Book
from .serializer import AuthorSerializer,BookSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET','POST'])
def author_list_create(request):
    if request.method == 'GET':
        authors = Author.objects.all()#-->list of dictionary pabo ekhan theke
        #eita theke json e convert korbo serializer diye
        serializer = AuthorSerializer(authors,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    #client data
    elif request.method == 'POST':
        serializer = AuthorSerializer(data = request.data)#AuthorForm(request.POST) form theke post request paitam
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def book_list_create(request):
    if request.method == 'GET':
        authors = Book.objects.all()#-->list of dictionary pabo ekhan theke
        #eita theke json e convert korbo serializer diye
        serializer = BookSerializer(authors,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #client data
    elif request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def book_details(request,id):
    # try:
    #     book = Book.objects.get(id=id)
    # except Book.DoesNotExist:
    #     return Response({
    #         "error":"Book not found"
    #     },
    #     status=status.HTTP_404_NOT_FOUND) 
    
    #alternate of try catch
    book = get_object_or_404(Book, id=id)
        
    serializer = BookSerializer(book)
    return Response(serializer.data,status=status.HTTP_200_OK)

#CRUD with viewSet:
class AuthorViewSet(viewsets.ModelViewSet):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name','bio']
    ordering_fields = ['name']
    
    # permission_classes = [IsAuthenticated]
