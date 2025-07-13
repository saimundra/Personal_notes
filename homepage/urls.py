from django.urls import path
from . import views

urlpatterns = [
    path("", views.getnotes, name="allnotes"),
    path("update/<int:note_id>/", views.update_note, name="update_note"),
    path("delete/<int:note_id>/", views.delete_note, name="delete_note"),
]   