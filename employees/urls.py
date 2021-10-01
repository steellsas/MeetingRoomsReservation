from django.urls import path
from employees.views import EmployeeViewSet

app_name = 'employees'


urlpatterns = [
    path('employee/register', EmployeeViewSet.as_view({'post': 'create'})),
]