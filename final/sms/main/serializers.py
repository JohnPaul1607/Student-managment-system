from rest_framework import serializers
from.models import Student,Teacher

class studentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Student
        fields='__all__'
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'