from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RacePostViewSet

router = DefaultRouter()
router.register(r'posts', RacePostViewSet)

urlpatterns = router.urls