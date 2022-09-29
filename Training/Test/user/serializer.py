from dataclasses import field
from rest_framework import serializers
from .models import Laptops, Person, Product, Team, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Laptops
        fields="__all__"

class PersonSerializer(serializers.ModelSerializer):
    laptop=LaptopSerializer()
    class Meta:
        model=Person
        fields="__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields="__all__"



class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields="__all__"