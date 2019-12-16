from django.shortcuts import render
from .models import  Alumno
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def services(request):
    return render(request, 'app/services.html')

def projects(request):
    context= {
    'alumnos': Alumno.objects.all()
    }
    return render(request, 'app/projects.html',context)

def testimony(request):
    return render(request, 'app/testimony.html')

def contact(request):
    return render(request,'app/contact.html')
