from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import project
from .form import ProjectForm

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


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, 'projects/project_form.html',context)


def update_project(request, pk):
    prt = project.objects.get(id=pk)
    form = ProjectForm(instance = prt)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=prt)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, 'projects/project_form.html',context)


def delete_project(request, pk):
    ptr = project.objects.get(id=pk)
    if request.method == 'POST':
        ptr.delete()
        return redirect('projects')
    context = {'object':ptr}
    return render(request, 'projects/delete.html',context)