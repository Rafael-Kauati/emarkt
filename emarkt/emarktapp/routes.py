from django.urls import path
from . import views

#URL conf
urlpatterns = [
    path('greet/', views.greet),
    path('', views.greet, name='home'),
]