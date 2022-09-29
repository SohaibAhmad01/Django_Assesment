from rest_framework.views import APIView
from ..models import Blogs
from ..serializer import BlogSerializer
from rest_framework.response import Response


class BlogAPIView(APIView):
    def get(self, request):
        blogs = Blogs.objects.all()
        serializer = BlogSerializer(blogs, many=True)

        return Response({
            'sucess': True,
            'message': ' Get request fulfilled',
            'data': serializer.data

        })

    def post(self, request, *args, **kwargs):
        if request.data.get('title') != '':
            serializer = BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'sucess': True,
                    'message': ' POST request fulfilled',
                    'data': serializer.data

                })

    def put(self, request, *args, **kwargs):

        if request.data.get('id') is not None:
            blog = Blogs.objects.get(pk=request.data.get('id'))
            if blog:
                serializer = BlogSerializer(blog, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response ({
                        'sucess': True,
                        'message': ' Blog get updated request fulfilled',
                        'data': serializer.data

                    })
        return Response({
            'success':True,
            'message':' put request get successful',
            'data': ''
        })

    def delete(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            blog = Blogs.objects.get(pk=request.data.get('id'))
            if blog:
                blog.delete()
                return Response ({
                    'Success': True,
                    'message': ' delete blog post '
                })

        return Response ({
            'Success': True,
            'message': ' delete request fullfiled',
            'data': ''
        })
