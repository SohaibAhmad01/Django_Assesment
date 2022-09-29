from django.urls import path,include
from .views import PersonViewset, ProfileViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('profile',ProfileViewset),
router.register('person', PersonViewset),

urlpatterns=[
    path('', include(router.urls))
]
urlpatterns += router.urls