from tkinter import CASCADE
from django.db import models

# Create your models here.

class Profile(models.Model):
    display_name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    email=models.EmailField()


    def __str__(self) -> str:
        return self.display_name


class Hobby(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='user_hobby', null=True, blank=True)
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=400)


class Interest(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

class City(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Person(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.IntegerField()
    interest=models.ManyToManyField(Interest)

    def __str__(self) -> str:
        return self.name

class Address(models.Model):
    person=models.OneToOneField(Person, on_delete=models.CASCADE)
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    street_address=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.person.name + "("+self.street_address + ")"