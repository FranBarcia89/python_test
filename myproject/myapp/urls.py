from django.urls import path, include
from rest_framework import routers
from .views import CharacterViewSet
from .views import my_view

router = routers.DefaultRouter()
router.register(r'characters', CharacterViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('search-character-appearance', my_view)
]
