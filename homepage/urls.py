from django.urls import path
from . import views

urlpatterns =[
    path("",views.getnotes,name= "allnotes")
    
]