from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Blogs
from ..serializer import BlogSerializer


@api_view(['GET', 'POST'])
def blog_view(request):
    if request.method == 'GET':
        blogs = Blogs.objects.all()
        serializer = BlogSerializer(blogs, many=True)

        return Response({
            'sucess': True,
            'message': ' Get request fulfilled',
            'data': serializer.data

        })

    if request.method == 'POST':
        return Response({
            'sucess': True,
            'message': ' POST request fulfilled',
            'data': ''

        })

    return Response({
        'sucess': False,
        'message': '  request  can not  fulfilled',
        'data': ''

    })
