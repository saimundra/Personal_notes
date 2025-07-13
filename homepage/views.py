from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from addnotes.models import Allnotes

# Create your views here.
def getnotes(request):
    notes = Allnotes.objects.all()
    if request.method == "GET":
        return render(request,"notes.html",{"notes":notes})
    
def update_note(request, note_id):
    note = get_object_or_404(Allnotes, id=note_id)
    if request.method == 'POST':
        note.topic = request.POST.get('topic')
        note.date = request.POST.get('date')
        note.description = request.POST.get('description')
        
        # Handle image upload
        if 'image' in request.FILES:
            note.image = request.FILES['image']
        
        note.save()
        return redirect('allnotes')  # Redirect to the notes list view
    # For GET requests, redirect back to notes list
    return redirect('allnotes')

def delete_note(request, note_id):
    note = get_object_or_404(Allnotes, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('allnotes')  # Redirect to the notes list view
    # For GET requests, redirect back to notes list
    return redirect('allnotes')
