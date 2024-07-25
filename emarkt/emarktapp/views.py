# emarktapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import SignUpForm

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

def success(request):
    return HttpResponse("Registration successful!")
