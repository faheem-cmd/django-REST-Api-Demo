from rest_framework import serializers
# from rest_framework import employees
from . models import employees

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'
