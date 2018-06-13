from django.shortcuts import render
from .models import Note
from notes.serializers import NoteSerializer
from rest_framework import generics

class NoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

def index(request):
    #debugger import pdb; pdb.set_trace() 
    context = {}
    # pbid = PersonalBookmark.objects.values_list('id')
    # context['bookmarks'] = Bookmark.objects.exclude(id__in=pbid)

    if request.user.is_anonymous:
        context['notes'] = Note.objects.all()
    else:
        context['notes'] = Note.objects.filter(user=request.user)
    
    return render(request, 'notes/index.html', context)