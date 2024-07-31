from django.urls import path
from . import views

#URL conf
urlpatterns = [
    path('greet/', views.greet),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success, name='success'),
]