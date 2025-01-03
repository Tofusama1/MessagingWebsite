from rest_framework.routers import DefaultRouter
from api.api.urls import post_router
from django.urls import path, include
from . import views

router = DefaultRouter()
#posts
router.registry.extend(post_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]