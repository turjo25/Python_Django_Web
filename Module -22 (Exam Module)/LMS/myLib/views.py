from django.shortcuts import render,redirect,get_object_or_404
from .models import Book,Comment,Category,Tag,Author
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegForm,UserUpdateForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
def book_list(request):
    categoryQ = request.GET.get('category')
    tagQ = request.GET.get('tag')
    searchQ = request.GET.get('q')
    
    books = Book.objects.all() #shb post k anlam
    if categoryQ:
        books = books.filter(category__name = categoryQ) 
    if tagQ:
        books = books.filter(tag__name = tagQ)
    if searchQ:
        books = books.filter(
            Q(title__icontains = searchQ)|
            Q(description__icontains = searchQ)|
            Q(category__name__icontains = searchQ)|
            Q(tag__name__icontains = searchQ)|
            Q(authors__name__icontains=searchQ)
        ).distinct()
    
    paginator = Paginator(books,3) 
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
    return render(request,'booksf/book_list.html',context)

@login_required
def add_book(request):
    if  request.method == 'POST':
        form = forms.BookCreationForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit = False)
            # book.author = request.user
            book.save()
            return redirect('book_list')
    else:
        form = forms.BookCreationForm()
        
    return render(request,'booksf/book_form.html',{'form':form})

@login_required
def book_update(request,id):
    book = get_object_or_404(Book,id = id)
    if  request.method == 'POST':
        form = forms.BookCreationForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = forms.BookCreationForm(instance=book)
        
    return render(request,'booksf/book_form.html',{'form':form})

def book_delete(request,id):
    book = get_object_or_404(Book, id = id)
    book.delete()
    return redirect('book_list')

@login_required
def book_details(request, id):
    book = get_object_or_404(Book, id=id)
    
    # comment form handle
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.book = book
            comment.save()
            return redirect('book_details', id=book.id)
    else:
        form = forms.CommentForm()
    
    # show comments
    comments = book.comment_set.all()
     
    context = {
        'book' : book,
        'categories' : Category.objects.all(),
        'tag' : Tag.objects.all(),
        'comments' : comments,
        'comment_form' : forms.CommentForm
    }
    
    book.view_content += 1
    book.save()
    return render(request, 'booksf/book_detail.html', context)

def signup_view(request):
    if  request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('book_list')
    else:
        form = UserRegForm()
        
    return render(request,'users/signup.html',{'form':form})


@login_required
def profile(request):
    return render(request, "users/profile.html", {"user": request.user})

@login_required
def update_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")  # go back to task list after update
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "users/update_profile.html", {"form": form})

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user,data = request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password Changed!')
            return redirect('book_list')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request,'users/pass_change.html',{'form':form})