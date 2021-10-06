from django.urls import path
from employees.views import EmployeeViewSet

app_name = 'employees'

urlpatterns = [
    path('employee/register/', EmployeeViewSet.as_view({'post': 'create'}),name='employee_register'),
    path('employee/all/', EmployeeViewSet.as_view({'get': 'list'},name ='employees_list')),
    path('employee/detail/<int:pk>', EmployeeViewSet.as_view({'get': 'retrieve', 'put':'update'}, name='employees_list'))

]
