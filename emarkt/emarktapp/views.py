# emarktapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import SignUpForm
from .forms import LoginForm
def greet(request):
    return render(request, 'greet.html')

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success')  # Redirect to a success page after registration
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username_or_email')
            password = form.cleaned_data.get('password')
            
            # Try to authenticate by username
            user = authenticate(request, username=username_or_email, password=password)
            
            if user is None:
                # Try to authenticate by email
                try:
                    user_with_email = User.objects.get(email=username_or_email)
                    user = authenticate(request, username=user_with_email.username, password=password)
                except User.DoesNotExist:
                    pass
            
            if user is not None:
                login(request, user)
                return redirect('success')  # Redirect to a success page after login
            else:
                form.add_error(None, "Invalid username/email or password")
    else:
        form = LoginForm()
    return render(request, 'Login.html', {'form': form})

def success(request):
    return HttpResponse("Registration successful!")
