from django.urls import path
from . import views
app_name ='app'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('alumnos/', views.AlumnosListView.as_view(), name='alumnos'),
    path('alumnos/paquetes/<slug:id>/',views.paquetes,name='paquetes'),
    path('alumnos/paquetes/<slug:student_id>/<slug:paquete_id>/',views.clases,name='clases'),
    path('services/', views.services, name='services'),
    path('testimony/', views.testimony, name='testimony')
]
