from django.urls import path
from . import views
app_name ='app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('testimony/', views.testimony, name='testimony'),
    path('contact/', views.contact, name='contact'),
]
