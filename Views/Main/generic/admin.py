from django.contrib import admin

# Register your models here.
from .models import Blogs
from .models import Author, Book
admin.site.register(Blogs)
admin.site.register(Book)
admin.site.register(Author)
