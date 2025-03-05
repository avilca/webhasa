from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Project

# Create your views here.
def proyectos(request):
    projects = Project.objects.order_by('-created')

    #Paginador de 6 en 6
    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page', 1)
    projects = paginator.page(page_number)

    return render(request, 'project/proyectos.html',
                  {'projects': projects})