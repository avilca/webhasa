from django.shortcuts import render
from .models import Project

# Create your views here.
def proyectos(request):
    projects = Project.objects.all()

    return render(request, 'project/proyectos.html',
                  {'projects': projects})