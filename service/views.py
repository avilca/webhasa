from django.shortcuts import render
from .models import Service

# Create your views here.

def servicios(request):
    services = Service.objects.all()

    return render(request, 'service/servicios.html',
                  {'services': services})

