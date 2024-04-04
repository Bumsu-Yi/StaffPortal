from django.urls import path
from .views import EmployeeDetail, JobHistoryList, DepartmentWithLocationList, SalaryIncreaseAPIView

urlpatterns = [
    path('employee/<int:employee_id>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('jobhistory/<int:employee_id>/', JobHistoryList.as_view(), name='jobhistory-list'),
    path('departments/', DepartmentWithLocationList.as_view(), name='department-location-list'),
    path('departments/<int:department_id>/increase-salary/', SalaryIncreaseAPIView.as_view(), name='increase-salary'),
]
