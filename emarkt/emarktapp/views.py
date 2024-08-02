# emarktapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm, SignUpForm
from .forms import LoginForm
def greet(request):
    return render(request, 'greet.html')

# -------- Products  --------

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product_edit.html', {'form': form})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # Ensure the current user is the owner of the product
    if product.owner != request.user:
        return redirect('product_detail', pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'product_edit.html', {'form': form})

# -------- Auth  --------

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
                return redirect('product_list')  # Redirect to a success page after login
            else:
                form.add_error(None, "Invalid username/email or password")
    else:
        form = LoginForm()
    return render(request, 'Login.html', {'form': form})

def success(request):
    return HttpResponse("Registration successful!")
