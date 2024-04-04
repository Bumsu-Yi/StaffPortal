from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employees, JobHistory, Departments
from .serializers import EmployeeSerializer, JobHistorySerializer, DepartmentWithLocationSerializer, SalaryIncreaseSerializer
from decimal import Decimal

class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'employee_id'

class JobHistoryList(generics.ListAPIView):
    serializer_class = JobHistorySerializer
    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        queryset = JobHistory.objects.filter(employee_id=employee_id).values('employee_id', 'start_date', 'end_date', 'job_id', 'department_id')
        return queryset

class DepartmentWithLocationList(generics.ListAPIView):
    queryset = Departments.objects.select_related('location').all() 
    serializer_class = DepartmentWithLocationSerializer

class SalaryIncreaseAPIView(generics.UpdateAPIView):
    serializer_class = SalaryIncreaseSerializer

    def get_queryset(self):
        department_id = self.kwargs['department_id']
        return Employees.objects.filter(department_id=department_id)

    def update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        salary_increase_rate = request.data.get('salary_increase_rate')
        if salary_increase_rate is None:
            return Response({"error": "salary_increase_rate parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        
        for employee in queryset:            
            employee.salary = ((employee.salary) * Decimal(1 + salary_increase_rate))
            employee.save()
        
        return Response({"message": "Salaries increased successfully."}, status=status.HTTP_200_OK)