from rest_framework import serializers
from .models import Blogs, Book, Author


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']


class AuthorSerializer(serializers.ModelSerializer):
    allBooks = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'Age', 'allBooks']
