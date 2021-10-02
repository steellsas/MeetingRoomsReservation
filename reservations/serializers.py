# from rest_framework import serializers
# from django.contrib.auth.models import User
# from employees.serializers import EmployeeSerializer
# from employees.models import Employee
# from reservations.models import EmployeesInMeetingRoom, MeetingRoomReservation
#
#
# class EmployeesInMeetingRoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeesInMeetingRoom
#         fields = "__all__"
#         depth = 1
#
#
# class EmployeesGroupSerializer(serializers.ModelSerializer):
#     employee = EmployeeSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = EmployeesInMeetingRoom
#         fields = "__all__"
#
#         def create(self, validated_data):
#
#             employee_group = self.validated_data.get('employee', [])
#             if isinstance(employee_group, list):
#                 for empl_id in employee_group:
#                     try:
#                         employees = Employee.objects.get(pk=empl_id)
#                         EmployeesInMeetingRoom.employee.add(employees)
#                     except Exception as err:
#                         pass
#             return EmployeesInMeetingRoom
#
#         def update(self, instance, validated_data):
#             # instance.title = validated_data.get('title', instance.title)
#             # instance.price = validated_data.get('price', instance.price)
#             # instance.published = validated_data.get('published', instance.published)
#             # instance.save()
#
#             employee = self.initial_data.get("authors", [])
#             print('darbuotoju grupe',employee)
#             if isinstance(employee, list):
#                 if len(employee) > 0:
#                     # delete previous auth
#                     instance.employee.clear()
#
#                     # preAuths = instance.authors.all()
#                     # for auth in preAuths:
#                     #     instance.authors.remove(auth)
#
#                     # set new auth
#                     for authID in employee:
#                         print(authID)
#                         try:
#                             empl = Employee.objects.get(pk=authID)
#                             instance.employee.add(empl)
#                         except Exception as err:
#                             pass
#             return instance
#
#
#
#
#
#
#
#
#
#
#
#
