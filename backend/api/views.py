from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note
# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer #we pass to serializer diff data and it tells if its valid or not(compare with model(for example check if title shorter than 100))
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user # gonna give us the user who is creating a note
        return Note.objects.filter(author=user) #give us all the notes written by the user
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user) # так как author is readonly (in serializer) we have to specify the author by modifying the serializer
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): # to make sure we delete the notes that we created/own
        user = self.request.user # gonna give us the user who is creating a note
        return Note.objects.filter(author=user) #give us all the notes written by the user

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #here are all objects we have to make sure we dont create the same one
    serializer_class = UserSerializer # what kind of data we need to accept (usrname and password)
    permission_classes = [AllowAny] #who can call this view in this case anyone even if they are not authanticated

