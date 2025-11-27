
from django.contrib import admin
from django.urls import path
from careapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

     path('', views.index, name='index'),

     path('starter/', views.starter, name='starter'),

     path('about/', views.about, name='about'),

      path('services/', views.services, name='services'),

      path('appointment/', views.Appoint, name='appointment'),

      path('department/', views.Depart, name='department'),

      path('show/', views.show, name='show'),



]
