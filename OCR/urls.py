"""OCR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from course.views import home
from course.views import function,register,login,about,new,student,contact,register1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('course/',function),
    path('templates/register.html',register),
    path('templates/register1.html',register1),
    path('templates/login.html',login),
    path('templates/about.html',about),
    path('templates/available.html',function),
    path('templates/new.html',new),
    path('templates/student.html',student),
    path('templates/contact.html',contact)
    
    

    
]

