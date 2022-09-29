from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .models import Person, Product, Team, User
from .serializer import PersonSerializer, ProductSerializer, TeamSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import status
# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=(IsAuthenticated,)


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
        


class PersonView(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    permission_classes=(IsAdminUser,)


class TeamView(viewsets.ModelViewSet):
    queryset=Team.objects.all()
    serializer_class=TeamSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)


class ProductView(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=(IsAuthenticated,)
        
        
    def create(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        user=request.user
        user_id=request.user.id
        request.data['user_id']=user_id
        print(request.data)
        import pdb; pdb.set_trace()
        data=ProductSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        
        return Response(data)
        
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # import pdb; pdb.set_trace()
        print(instance.user_id.id)
        print(request.user.id)
        import pdb; pdb.set_trace()
        print(request.data)
        if instance.user_id.id == request.user.id:
            request.data['user_id'] = instance.user_id.id
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        

        return Response('')

        
        
        



    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()

    # def get_success_headers(self, data):
    #     try:
    #         return {'Location': str(data[api_settings.URL_FIELD_NAME])}
    #     except (TypeError, KeyError):
    #         return {}

        

    


