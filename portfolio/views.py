from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all() # grab data from Project database
    return render(request, 'portfolio/home.html', {'projects':projects})
