''' from django.shortcuts import render

# Create your views here.
# api_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializer

class StudentListCreateAPIView(APIView):
    """
    GET: list all students
    POST: create a new student
    """
    def get(self, request):
        students = Student.objects.all().order_by('-created_at')
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailAPIView(APIView):
    """
    GET: retrieve a student
    PUT: update entire student
    PATCH: partial update
    DELETE: delete student
    """
    def get_object(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
# Authentication not Required
'''
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny  # <- BOTH imported
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet gives list/retrieve/create/update/destroy by default.
    """
    queryset = Student.objects.all().order_by("-created_at")
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]  # default permission

    # Example: public read, only authenticated create/update/delete
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated()] '''

# Authentication Required
'''
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Student model
    All endpoints require authentication (JWT or Browsable API login)
    """
    queryset = Student.objects.all().order_by("-created_at")
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]  # enforce authentication

'''

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    Student CRUD API

    - list/retrieve: optionally public (AllowAny) or authenticated
    - create/update/delete: authenticated only
    - Works with JWT (for API clients) and SessionAuthentication (for browser)
    """
    queryset = Student.objects.all().order_by("-created_at")
    serializer_class = StudentSerializer

    # Option A: Require authentication for ALL actions (simplest)
    # permission_classes = [IsAuthenticated]

    # Option B: Public read, login required for write
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]      # anyone can view
        return [IsAuthenticated()]   # create/update/delete requires login
