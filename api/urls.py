from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ApplicationViewset

router = DefaultRouter()
router.register(r'api/v1/apply', ApplicationViewset, basename='application')


urlpatterns = [
    path('', include(router.urls)),
]