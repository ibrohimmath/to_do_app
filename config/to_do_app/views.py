from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404 
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView

from django.urls import reverse, reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreateForm 

from .models import Task 

import datetime

class SignUpView(CreateView):
    form_class = UserCreateForm 
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'

class DashboardView(LoginRequiredMixin, ListView):
    model = Task 
    template_name = 'home.html'
    
    def get_queryset(self):
        # print(self.request.user.username)
        return super().get_queryset().filter(owner = self.request.user)
            
# Functional task createing view
# def taskCreateView(request):
#     if request.method == 'POST':
#         description = request.POST['description']
#         owner = request.user
#         deadline = request.POST['deadline']
#         if description:
#             new_task = Task.objects.create(
#                 description = description, 
#                 owner = owner,
#                 deadline = deadline,
#             )
#     return redirect(reverse_lazy('home'))

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy('home')
    fields = ['description', 'deadline']
    template_name = 'home'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        
# Functional task deleting view        
# def taskDeleteView(request, id):
#     task = Task.objects.get(id = id)
#     task.delete()
#     return redirect(reverse_lazy('home'))

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task 
    success_url = reverse_lazy('home')
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
    
# Functional task changing view    
# def taskChangeView(request, id):
#     task = Task.objects.get(id = id)
#     task.done = 1
#     task.save()
#     return redirect(reverse_lazy('home'))    

class TaskChangeView(LoginRequiredMixin, DetailView):
    model = Task    
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.done = 1
        self.object.save()
        return redirect(reverse_lazy('home'))
         
    