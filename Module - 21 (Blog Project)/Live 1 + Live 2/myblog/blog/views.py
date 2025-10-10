from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment,Category,Tag
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.
#Post List:
#category,tag,search

def post_list(request):
    categoryQ = request.GET.get('category')
    tagQ = request.GET.get('tag')
    searchQ = request.GET.get('q')
    
    posts = Post.objects.all() #shb post k anlam
    if categoryQ:
        posts = posts.filter(category__name = categoryQ) #category__name = models.py -> Category class -> category variable -> name 
    if tagQ:
        posts = posts.filter(tag__name = tagQ)
    if searchQ:
        posts = posts.filter(
            Q(title__icontains = searchQ)|
            Q(content__icontains = searchQ)|
            Q(category__name__icontains = searchQ)|
            Q(tag__name__icontains = searchQ)
        ).distinct()
    
    paginator = Paginator(posts,2) #per page e 2 ta post
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'search_query': searchQ,
        'category_query': categoryQ,
        'tag_query': tagQ,
    }
    return render(request,'blog/post_list.html',context)

@login_required
def post_create(request):
    if  request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = forms.PostForm()
        
    return render(request,'blog/post_create.html',{'form':form})

@login_required
def post_update(request,id):
    post = get_object_or_404(Post,id = id)
    if  request.method == 'POST':
        form = forms.PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = forms.PostForm(instance=post)
        
    return render(request,'blog/post_create.html',{'form':form})

@login_required
def post_delete(request,id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('post_list')

@login_required
def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    
    # comment form handle
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_details', id=post.id)
    else:
        form = forms.CommentForm()
    
    # show comments
    comments = post.comment_set.all()
    is_liked = post.liked_users.filter(id=request.user.id).exists()
    like_count = post.liked_users.count()
    # liked part
    # like count
    
    context = {
        'post' : post,
        'categories' : Category.objects.all(),
        'tag' : Tag.objects.all(),
        'comments' : comments,
        'is_liked' : is_liked,
        'like_count' : like_count,
        'comment_form' : forms.CommentForm
    }
    
    post.view_content += 1
    post.save()
    return render(request, 'blog/post_details.html', context)

@login_required
def like_post(request,id):
    post = get_object_or_404(Post,id=id)

    if post.liked_users.filter(id=request.user.id):
        post.liked_users.remove(request.user)#user like diye thake thahole eita abar press krle remove hoye jabe
    else:
        post.liked_users.add(request.user)#user jde like na diye thake thahole eita  press krle like hoye jabe
    
    return redirect('post_details',id=post.id)

def signup_view(request):
    if  request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
        
    return render(request,'user/signup.html',{'form':form})

# Profile page
@login_required
def profile_view(request):
    section = request.GET.get('section', 'profile')
    context = {'section' : section}#evabeo context build kora jay..first e declare korbo trpor shb update korbo
    
    if section == 'posts':
        posts = Post.objects.filter(author = request.user)
        context['posts'] = posts #context update hocce 
    
    elif section == 'update':
        if request.method == 'POST':
            form = forms.UpdateProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('/profile?section=update')
        else:
            form = forms.UpdateProfileForm(instance=request.user)
    
        context['form'] = form #context update hocce 
    
    return render(request, 'user/profile.html', context)