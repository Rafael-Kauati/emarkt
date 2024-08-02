from django.urls import path
from . import views

#URL conf
urlpatterns = [
    path('greet/', views.greet),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/new/', views.product_new, name='product_new'),
    path('success/', views.success, name='success'),

]