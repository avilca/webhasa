from django.shortcuts import render, HttpResponse


# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def servicios(request):
    return render(request, 'core/servicios.html')

