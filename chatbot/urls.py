from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatHistoryViewSet

router = DefaultRouter()
router.register(r'history', ChatHistoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
