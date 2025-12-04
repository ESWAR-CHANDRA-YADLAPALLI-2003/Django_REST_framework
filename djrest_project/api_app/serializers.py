# api_app/serializers.py
# Serializer converts Model ↔ JSON and validates input.
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'roll_no', 'created_at']
        read_only_fields = ['id', 'created_at']
