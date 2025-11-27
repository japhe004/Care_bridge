from django.contrib import admin
from careapp.models import *
from careapp.views import Appoint

#Register your models here.
admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)

