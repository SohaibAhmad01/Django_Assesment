from multiprocessing import context
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import  TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets

# Create your views here.

class HelloView(APIView):
    
    permission_classes=(IsAdminUser,)
    
    def get (self, request):
        # import pdb; pdb.set_trace()
        content = {'message': 'Hello, World!'}
        return Response(content)


class HiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class =
    permission_classes=(IsAuthenticated,)

    def get(self,request):
        return Response ("I am Phenominal")

class CustomToken(ObtainAuthToken):
    def post(self, request,*args, **krgs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'email':user.email,
        })


