from django.shortcuts import render,redirect
from .forms import loginForm,UserCreation
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import post
# Create your views here.

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        user = authenticate(request , username = username,password = password)

        if user is not None :
            login(request,user)
            return redirect('/')
        else:
            messages.error(request , 'password / username is incorrect')

    return  render(request , 'student/login.html')

def logoutPage(request):
    logout(request)
    return redirect('/login')

def registerPage(request):

    if request.method == 'POST':
        form = UserCreation(request.POST)

        if form.is_valid:
            try:
                form.save()
                return redirect('/login')
            except:
                messages.error(request ,form.errors)
                return redirect('/register')
    else:
        form = UserCreation()

    return render(request,'student/register.html',{'form' : form,})


def Index(request):
    return render(request ,'student/index.html')


def postView(request, postid):
    posts = post.objects.filter(pk__lt = 10*postid ).filter(pk__gte = 10*(postid-1)).filter(is_verified = True)
    
    return render(request, 'student/postView.html',{'posts' : posts,'id' : postid+1,})