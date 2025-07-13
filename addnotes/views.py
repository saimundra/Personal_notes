from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Allnotes

# Create your views here.
def addnote(request):
    if request.method == "GET":
        notes = Allnotes.objects.all()
        return render (request,'addnotes.html')
    elif request.method == "POST":
        topic = request.POST["topic"]
        date = request.POST["date"]
        description = request.POST["description"]
        
        # Handle image upload
        image = request.FILES.get('image')
        
        notes = Allnotes(topic=topic, date=date, description=description)
        if image:
            notes.image = image
        notes.save()
        return HttpResponseRedirect("/")
    else:
        return HttpResponse ("<h1>INVALID REQUEST METHOD </h1>") 

