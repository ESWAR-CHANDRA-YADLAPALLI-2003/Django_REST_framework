# api_app/urls.py
''''from django.urls import path
from .views import StudentListCreateAPIView, StudentDetailAPIView

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
]
'''
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r"students", StudentViewSet, basename="student")

urlpatterns = [
    path("", include(router.urls)),
]
