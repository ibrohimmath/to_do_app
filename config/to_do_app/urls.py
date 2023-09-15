from django.contrib import admin 
from django.urls import path, include 

from django.views.generic import TemplateView 

from . import views 

urlpatterns = [
    path('', views.DashboardView.as_view(), name = 'home'),
    path('new/', views.TaskCreateView.as_view(), name = 'create-task'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name = 'delete-task'),
    path('change/<int:pk>/', views.TaskChangeView.as_view(), name = 'change-task'),

    path('signup/', views.SignUpView.as_view(), name = 'signup'),
]