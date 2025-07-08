from django.shortcuts import render
from django.http import HttpResponse
from addnotes.models import Allnotes

# Create your views here.
def getnotes(request):
    notes = Allnotes.objects.all()
    if request.method == "GET":
        return render(request,"notes.html",{"notes":notes})