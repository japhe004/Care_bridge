from django.shortcuts import render

# Create your views here.
def  index(request):
    return render(request, 'index.html')

def  starter(request):
    return render(request, 'starter-page.html')

def  about(request):
    return render(request, 'about.html')

def  services(request):
    return render(request, 'services.html')

def  Appoint(request):
    return render(request, 'appointment.html')

def  Depart(request):
    return render(request, 'department.html')