from django.shortcuts import render
from rest_framework import viewsets
from .models import Person, Profile
from .serializer import PersonSerializer, ProfileSerializer

# Create your views here.


class ProfileViewset(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    http_method_names= ['get','post','retrieve','put','patch','delete']

class PersonViewset(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    http_method_names= ['get','post','retrieve','put','patch','delete']
    