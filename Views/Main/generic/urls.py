from django.contrib import admin
from django.urls import path, include
from generic.View.fn_view import blog_view
from generic.View.classapi import BlogAPIView
from generic.View.genericapi import BlogListCreateAPIView
from generic.View.genericapi import BlogRetrieveUpdateDestroyAPIView
from generic.View.viewsetapi import BlogViewSets
from generic.View.viewsetapi import BlogModeViewSet,AuthorViewSet,BookViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ubcv', BlogModeViewSet)

router.register(r'book', BookViewSet)
router.register(r'Author', AuthorViewSet)

blog_list = BlogViewSets.as_view({
    'get': 'list'
})
blog_detail = BlogViewSets.as_view({
    'get': 'retrieve'
})

# advance
# blog_lists = BlogModeViewSet.as_view({
#     'get': 'list',
# })
# blog_details = BlogModeViewSet.as_view({
#     'get': 'retrieve'
# })
# blog_update = BlogModeViewSet.as_view({
#     'put': 'update'
# })

urlpatterns = [
    path('', include(router.urls)),
    path('fbv', blog_view),
    path('cbv', BlogAPIView.as_view()),
    path('gbv', BlogListCreateAPIView.as_view()),
    path('gbv/<int:pk>', BlogRetrieveUpdateDestroyAPIView.as_view()),
    ##with custom logic in viewset
    path('vbc', blog_list),
    path('vbc/<int:pk>', blog_detail),

    ### more advance
    # path('uvbc', blog_lists),
    # path('uvbc/<int:pk>', blog_details),
    # path('uvbc/<int:pk>', blog_update),




]
urlpatterns += router.urls