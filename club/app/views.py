from django.shortcuts import render
from .models import  Alumno
from .models import Paquete_Inscrito
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def services(request):
    return render(request, 'app/services.html')

def alumnos(request):
    context= {
    'alumnos': Alumno.objects.all()
    }
    return render(request, 'app/alumnos.html',context)

def paquetes(request,id):
    student = Alumno.objects.all().get(id=id)
    paquetes = []
    for paquete in student.paquete_inscrito_set.all():
        paquetes.append(paquete)
    context = {
    'student' : student,
    'paquetes': paquetes
    }
    print(context)
    return render(request,'app/paquetes.html',context)

def clases(request,student_id,paquete_id):
    student = Alumno.objects.all().get(id=student_id)
    paquete  = Paquete_Inscrito.objects.all().get(id=paquete_id)
    clases = []
    for clase in paquete.sesiones.all() :
        clases.append(clase)

    context = {
        'student':student,
        'clases': clases
         }
    return render(request,'app/clases.html',context)

def testimony(request):
    return render(request, 'app/testimony.html')

def contact(request):
    return render(request,'app/contact.html')
