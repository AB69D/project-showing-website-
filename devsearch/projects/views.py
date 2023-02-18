from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def projects(request):
    projects = Project.objects.all()
    contest = {'projects': projects}
    return render(request,'projects/projects.html',contest) 

def project(request,pk):
    return render(request,'projects/single_project.html')