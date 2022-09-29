from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return  self.name

class Product(models.Model):
    user_id=models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name