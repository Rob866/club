from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def services(request):
    return render(request, 'app/services.html')

def projects(request):
    return render(request, 'app/projects.html')

def testimony(request):
    return render(request, 'app/testimony.html')

def contact(request):
    return render(request,'app/contact.html')
