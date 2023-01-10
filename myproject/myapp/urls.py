from django.urls import path, include
from rest_framework import routers
from .views import CharacterViewSet
router = routers.DefaultRouter()
router.register(r'mymodel', CharacterViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
