"""adminpannel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basictable/',basictable),
    path('blank/',blank),
    path('buttons/',buttons),
    path('calendar/',calendar),
    path('chartjs/',chartjs),
    path('formcomponent/',formcomponent),
    path('gallery/',gallery),
    path('general/',general),
    path('lockscreen/',lockscreen),
    path('login/',login),
    path('morris/',morris),
    path('panels/',panels),
    path('responsivetable/',responsivetable),
    path('todolist/',todolist),
    path('adminlogin/',adminlogin),
    path('error/',error),
    path('addvendor/',addvendor),
    path('addproduct/',addproduct),
    path('addproductcategory/',addproductcategory),
]
