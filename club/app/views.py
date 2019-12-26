from django.shortcuts import render
from .models import  Alumno
from .models import Paquete_Inscrito
from django.db.models import Q
from django.templatetags.static import static
from django.conf import settings
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def services(request):
    return render(request, 'app/services.html')


class AlumnosListView(ListView):
    template_name= 'app/alumnos.html'
    context_object_name = 'alumnos'

    def get_queryset(self):
        if 'busqueda' in self.request.GET:
            query = self.request.GET.get('busqueda')
            if query:
                return Alumno.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query)).order_by('apellido')
        return  None

def paquetes(request,id):
    student = Alumno.objects.all().get(id=id)
    paquetes = []
    for paquete in student.paquete_inscrito_set.all():
        paquetes.append(paquete)
    context = {
    'student' : student,
    'paquetes': paquetes
    }
    return render(request,'app/paquetes.html',context)

def clases(request,student_id,paquete_id):
    student = Alumno.objects.all().get(id=student_id)
    paquete  = Paquete_Inscrito.objects.all().get(id=paquete_id)
    clases = []
    for clase in paquete.sesiones.all() :
        clases.append(clase)

    context = {
        'student':student,
        'clases': clases,
        'paquete':paquete
         }
    return render(request,'app/clases.html',context)

def testimony(request):
    return render(request, 'app/testimony.html')
