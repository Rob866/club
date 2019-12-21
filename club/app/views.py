from django.shortcuts import render
from .models import  Alumno
from .models import Paquete_Inscrito
from .models import Post
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

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def services(request):
    return render(request, 'app/services.html')

def blog(request):
    posts = Post.objects.filter(status=1).order_by('-create_on')
    context= {
    'posts': posts
    }
    return render(request,'app/blog.html',context)

def postDetail(request,id):
    post = Post.objects.all().get(id=id)
    context = {
    'post': post
    }
    return render(request,'app/detail_post.html',context)

class AlumnosListView(ListView):
    model = Alumno
    template_name= 'app/alumnos.html'
    context_object_name = 'alumnos'
    ordering =['-apellido']
    paginate_by= 10

    def get_queryset(self):
        if 'busqueda' in self.request.GET:
            query = self.request.GET.get('busqueda')
            if query:
                return Alumno.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query))
        return Alumno.objects.all().order_by('apellido')


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

def contact(request):
    return render(request,'app/contact.html')
