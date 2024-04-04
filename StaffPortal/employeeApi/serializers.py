from rest_framework import serializers
from .models import Employees, JobHistory, Departments

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        verbose_name_plural = "Employees"

class JobHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobHistory
        fields = '__all__'

class DepartmentWithLocationSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source='location.city')  # 위치 정보에서 도시 정보를 가져옵니다.

    class Meta:
        model = Departments
        fields = ['department_id', 'department_name', 'location']

class SalaryIncreaseSerializer(serializers.Serializer):
    salary_increase_rate = serializers.FloatField(min_value=0)