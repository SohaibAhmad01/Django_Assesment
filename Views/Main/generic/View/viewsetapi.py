from rest_framework import viewsets, status
from ..models import Blogs,Book,Author
from ..serializer import BlogSerializer, BookSerializer,AuthorSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAdminUser

### when we need custom logic
class BlogViewSets(viewsets.ViewSet):
    def list(self, request):
        queryset = Blogs.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

    ##return single item from list
    def retrieve(self, request, pk=None):
        queryset = Blogs.objects.all()
        if pk is not None:
            blog = get_object_or_404(queryset, pk=pk)
            serializer = BlogSerializer(blog)
            return Response(serializer.data)


###use already defined methods
class BlogModeViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = [IsAdminUser]



class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer


