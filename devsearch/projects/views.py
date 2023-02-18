from django.shortcuts import render
from django.http import HttpResponse
from .models import project

def projects(request):
    pts = project.objects.all()
    context = {'projects': pts}
    return render(request, 'projects/projects.html',context)

def single_project(request, pk):
    projectobj = project.objects.get(id = pk)
    tags = projectobj.tags.all() 
    context = {
        'project' : projectobj,
        'tags' : tags
    }
    return render(request,'projects/single_project.html',context)

