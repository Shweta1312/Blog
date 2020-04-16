from django.shortcuts import render
from .models import Profile
from .forms import UserForm
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def view_profile(request):
    profile = Profile.objects.get(user_name=request.user)
    return render(request, 'user_profile/view_profile.html', {'profile':profile})

def view_reg(request):
    if request.method == 'POST': 
        form = UserForm(request.POST, request.FILES)
        if form.is_valid(): 
            post=form.save(commit=False)
            post.user_name=request.user
            post.save() 
            return redirect('/')
        else:
            return HttpResponse("<h1>Fail</h1>")
    else: 
        form = UserForm() 
    return render(request,'user_profile/reg.html',{'form':form})