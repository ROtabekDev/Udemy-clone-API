from rest_framework import serializers 
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name'
        ]

class UserAuthSerializer(serializers.ModelSerializer):
    courses = serializers.ListField(source='get_all_courses')
    class Meta:
        model = User
        fields = ['name', 'id', 'courses', 'email']