from django.db import models


# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(blank=True, max_length=8000)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100, default='')
    Age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='allBooks')

    def __str__(self):
        return self.title
