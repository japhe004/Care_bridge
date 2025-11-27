from django.shortcuts import render,redirect

from careapp.models import Appointment
from django.contrib import messages

# Create your views here.
def  index(request):
    return render(request, 'index.html')

def  starter(request):
    return render(request, 'starter-page.html')

def  about(request):
    return render(request, 'about.html')

def  services(request):
    return render(request, 'services.html')
def Depart(request):
    return render(request, 'department.html')
def  Appoint(request):
    if request.method == 'POST':
        myappointment = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )
        myappointment.save()
        messages.success(request, 'Appointment has been added.')
        return redirect('/appointment')
    else:
        return render(request, 'appointment.html')

#fetching code
def show(request):
    all = Appointment.objects.all()
    return render(request, 'show.html',{"all": all})#keey and value


