from django.db import models
from django.db.models.fields import CharField


# Create your models here.

class Patient(models.Model):
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    visit_date = models.DateTimeField()
    medical_history = models.TextField()

def __str__(self):
    return self.firstname + ' ' + self.surname

class MedicalRecord(models.Model):
    patientname = models.CharField(max_length=20)
    doctor = models.CharField(max_length=50)
    diagnosis = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.patientname + '  attended by D.R. ' + self.doctor

    #model linking to the frontend
class Appointment(models.Model):
        name = models.CharField(max_length=20)
        email = models.EmailField()
        phone = models.CharField(max_length=10)
        date = models.DateTimeField()
        department = models.CharField(max_length=20)
        doctor = models.CharField(max_length=30)
        message = models.TextField()

        def __str__(self):
            return self.name