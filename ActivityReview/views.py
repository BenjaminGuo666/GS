from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Activity
from django.urls import reverse_lazy

class ActivityListView(ListView):
    model = Activity
    template_name = 'activities/list.html'

class ActivityCreateView(CreateView):
    model = Activity
    fields = ['title', 'description']
    template_name = 'activities/create.html'
    success_url = reverse_lazy('activity_list')

class ActivityUpdateView(UpdateView):
    model = Activity
    fields = ['title', 'description']
    template_name = 'activities/update.html'
    success_url = reverse_lazy('activity_list')

class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = 'activities/delete_confirm.html'
    success_url = reverse_lazy('activity_list')

# Create your views here.
