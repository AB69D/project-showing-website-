from django.shortcuts import render
from django.http import HttpResponse

def projects(request,pk):
    return render(request, 'projects/projects.html')

def project(request):
    return render(request,'projects/single_project.html')