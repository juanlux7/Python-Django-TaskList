# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tareas

# Create your views here.


def index(request):
    
    tareas = Tareas.objects.all().order_by('-created_at')[:10]

    context = {
        'tareas': tareas
    }

    return render(request, 'index.html', context)

def crearTarea(request):
    
    if(request.method == 'POST'):
        
        title = request.POST['title']
        text = request.POST['text']
        
        tarea = Tareas(title=title, body=text)
        tarea.save()

        return redirect('/')
    else:
        return render(request, 'index.html')

def borrarTarea(request, id):
    
    Tareas.objects.filter(id=id).delete()

    return redirect('/')
    
