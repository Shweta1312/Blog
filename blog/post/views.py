from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import UserForm, PostForm
from .models import Post

# Create your views here.
def home(request):
    p=Post.objects.all().order_by('-date')
    t=Post.objects.values('tag').distinct() 
    return render(request,'post/homepage.html',{'p':p,'t':t})

def sign_up(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('profile/reg')
    return render(request, 'post/sign_up.html',{'form':form})

def add_post(request):
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid(): 
            post=form.save(commit=False)
            post.user=request.user
            post.save() 
            return redirect('/')
        else:
            return HttpResponse("<h1>Fail</h1>")
    else: 
        form = PostForm() 
    return render(request, 'post/add_post.html', {'form' : form}) 

def log_in(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'post/log_in.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'post/log_in.html', {'error_message': 'Enter correct username or password'})
    return render(request, 'post/log_in.html')

def log_out(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'post/log_in.html',{'form':form})


def all_post(request):
    p=Post.objects.all().order_by('-date')
    t=Post.objects.values('tag').distinct()  
    return render(request,'post/allpost.html',{'t':t,'p':p})

def tag_post(request,tag):
    tag=str(tag)
    p=Post.objects.filter(tag=tag)
    return render(request,'post/tag_post.html',{'p':p,'tag':tag})


def post_detail(request,p_id):
    p_id=int(p_id)
    p=Post.objects.get(id=p_id)
    is_liked=False
    if p.likes.filter(id=request.user.id).exists():
        is_liked=True
    return render(request,'post/post_detail.html',{'p':p,'is_liked':is_liked,'total_likes':p.total_likes()})

def like(request,p_id):
    p=get_object_or_404(Post,id=request.POST.get('post_id'))
    is_liked=False
    if p.likes.filter(id=request.user.id).exists():
        p.likes.remove(request.user)
        is_liked=False
    else:
        p.likes.add(request.user)
        is_liked=True
    p_id=int(p_id)
    p=Post.objects.get(id=p_id)
    return render(request,'post/post_detail.html',{'p':p,'is_liked':is_liked,'total_likes':p.total_likes()})