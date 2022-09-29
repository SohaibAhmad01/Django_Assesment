from django.urls import path, include
from .views import PersonView, ProductView, TeamView, UserView,CustomToken

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'userlist', UserView)
router.register(r'personlist', PersonView)
router.register(r'teamlist', TeamView)
router.register(r'productlist', ProductView)


urlpatterns=[
    path('', include(router.urls)),
    path('register/',CustomToken.as_view()),
]
urlpatterns += router.urls