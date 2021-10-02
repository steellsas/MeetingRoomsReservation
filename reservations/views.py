from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response
# from reservations.models import EmployeesInMeetingRoom
# from employees.models import Employee
# from reservations.serializers import EmployeesInMeetingRoomSerializer, EmployeesGroupSerializer
#
#
# class EmployeeGroupViewSet(viewsets.ModelViewSet):
#     queryset = EmployeesInMeetingRoom.objects.all()
#     serializer_class = EmployeesGroupSerializer
#     permission_classes = []

#
# class EmployeesInMeetingRoomListView(viewsets.ModelViewSet):
#     serializer_class = EmployeesInMeetingRoomSerializer
#
#     def get_queryset(self):
#         employees_in_room = EmployeesInMeetingRoom.objects.all()
#         return employees_in_room
#
#     def create(self, request,*args,**kwargs):
#         data = request.data
#         new_employees_group = EmployeesInMeetingRoom.objects.create()
#         new_employees_group.save()
#
#         for empl in data['employee']:
#             employee_obj = Employee.objects.get(id=empl['id'])
#             new_employees_group.employee.add(employee_obj)
#         serializer = EmployeesInMeetingRoomSerializer(new_employees_group)
#         return Response(serializer.data)



# group = {'id': 50, 'employee': [{'id': 1}, {'id': 5}]}
