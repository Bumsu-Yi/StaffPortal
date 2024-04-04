from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employees, JobHistory, Departments
from .serializers import EmployeeSerializer, JobHistorySerializer, DepartmentWithLocationSerializer, SalaryIncreaseSerializer
from decimal import Decimal
import requests
from datetime import datetime
from rest_framework.exceptions import APIException

class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'employee_id'

class JobHistoryList(generics.ListAPIView):
    serializer_class = JobHistorySerializer
    
    def get_queryset(self):
        try:
            # URL에서 employee_id 가져오기
            employee_id = self.kwargs['employee_id']
            # employee_id에 해당하는 직무 이력 조회
            queryset = JobHistory.objects.filter(employee_id=employee_id).values('employee_id', 'start_date', 'end_date', 'job_id', 'department_id')
            return queryset
        except KeyError:
            # employee_id가 없을 경우 에러 발생
            raise APIException(detail="employee_id parameter is required.", code=status.HTTP_400_BAD_REQUEST)

class DepartmentWithLocationList(generics.ListAPIView):
    # 부서 및 위치 정보 조회 API
    queryset = Departments.objects.select_related('location').all() 
    serializer_class = DepartmentWithLocationSerializer

class SalaryIncreaseAPIView(generics.UpdateAPIView):
    # 급여 인상 API
    serializer_class = SalaryIncreaseSerializer

    def get_queryset(self):
        try:
            # URL에서 department_id 가져오기
            department_id = self.kwargs['department_id']
            # department_id에 해당하는 직원 조회
            return Employees.objects.filter(department_id=department_id)
        except KeyError:
            # department_id가 없을 경우 에러 발생
            raise APIException(detail="department_id parameter is required.", code=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        salary_increase_rate = request.data.get('salary_increase_rate')
        if salary_increase_rate is None:
            # salary_increase_rate가 없을 경우 에러 발생
            raise APIException(detail="salary_increase_rate parameter is required.", code=status.HTTP_400_BAD_REQUEST)
        
        # 선택된 부서의 모든 직원에 대해 연봉 인상 계산
        for employee in queryset:            
            employee.salary = ((employee.salary) * Decimal(1 + salary_increase_rate))
            employee.save()
        
        return Response({"message": "Salaries increased successfully."}, status=status.HTTP_200_OK)

class UVIndexAPIView(APIView):
    def get(self, request, area_no):
        current_time = datetime.now().strftime("%Y%m%d%H")

        url = 'http://apis.data.go.kr/1360000/LivingWthrIdxServiceV4/getUVIdxV4'
        params = {
            "serviceKey": "dMUvfo1w7O/j+0APsfGOkMBx+p05VNU1aIMLlZ4l4NTGzLxhdLILhOZ4t8lREYlQ4Ws0h4V6yO/NcPdq3WE+WA==",
            "areaNo": area_no,
            "time": current_time,
            "dataType": "JSON"
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # API 호출에 실패할 경우 에러 발생
            raise APIException(detail=f"Failed to fetch data from API: {str(e)}", code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        data = response.json()
        return Response(data, status=status.HTTP_200_OK)