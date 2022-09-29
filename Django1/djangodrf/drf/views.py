from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets

from django.http import JsonResponse
from rest_framework.response import Response


generics.ListCreateAPIView
# Create your views here.
@api_view(['GET'])
def Simple(request):
    return Response("sohaib")

