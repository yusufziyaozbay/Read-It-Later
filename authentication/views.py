from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'authentication/index.html')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # If passwords don't match
        if password1 != password2:
            error_message(request, 'Passwords do not match.')
        
        # If username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('/signup')
        
        # If mail already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('/signup')

        # Create user
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your account has been successfully created.')
        return redirect('/login')
    else:
        return render(request, 'authentication/user_signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            #return render(request, 'authentication/index.html', {'user': user})
            return redirect('/', {'user': user})
        
        else:
            messages.error(request, 'Invalid Credentials')
            #return redirect('/login')
            return render(request, 'authentication/user_login.html')
    
    else:
        return render(request, 'authentication/user_login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/')


def error_message(request, message):
    messages.error(request, message)
    return redirect('/signup')


