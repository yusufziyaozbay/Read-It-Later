from django.shortcuts import render, redirect
from django.conf import settings
from readitlater import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from . tokens import generate_token


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
            messages.error(request, 'Passwords do not match.')
            return redirect('/signup/')
        
        # If username is not alpha numeric
        if not username.isalnum():
            messages.error(request, 'Username must be alpha-numeric.')
            return render(request, 'authentication/user_signup.html')
        
        # If username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('/signup/')
        
        # If mail already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('/signup/')

        # Create user
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        messages.success(request, 'Your account has been successfully created.')

        # Welcome Email
        subject = "Welcome to Read It Later!"
        message = "Hi " + myuser.first_name + " " + myuser.last_name + ", \n" + "Welcome to Read It Later! \nThank you for being a member.\nWe have also sent you a confirmation email, please confirm your email adress in order to activate your account."
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Please confirm your email | Read It Later"
        message2 = render_to_string('email_confirmation.html',{
            'name' : myuser.first_name,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token' : generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        return redirect('/login/')
    
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
            return redirect('/home/', {'user': user})
        
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')
    
    else:
        return redirect('/')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        messages.success(request, 'Your account has been activated successfully')
        myuser.save()
        login(request, myuser)
        return redirect('/')
    else:
        return render(request, 'activation_failed.html')

