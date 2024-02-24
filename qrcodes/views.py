from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Activity

class ActivityListView(ListView):
    model = Activity
    template_name = 'activities/list.html'

class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activities/detail.html'

class ActivityCreateView(CreateView):
    model = Activity
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'activities/form.html'

class ActivityUpdateView(UpdateView):
    model = Activity
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'activities/form.html'

class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = 'activities/confirm_delete.html'
    success_url = '/activities/'

# Create your views here.
