
from django.contrib import admin
from django.urls import path, include
from patients import views as pview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('H-Manage/',include('patients.urls') ),
    path('account/',include('users_app.urls') ),
    path('',pview.index, name ='index'),
    path('contact',pview.contact, name ='contact'),
]
