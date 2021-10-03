from rest_framework import serializers
from reservations.models import RoomBooking
from rooms.serializers import MeetRoomSerializer
from employees.serializers import  EmployeeSerializer
from rooms.models import  MeetingRoom


class RoomBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomBooking
        fields = ('id','title', 'date_from', 'date_to', 'room', 'employees')
        # depth = 1


    # def create(self, validated_data):
    #     room_data = validated_data.pop('room_id')
    #     room_instance = MeetingRoom.objects.create(
    #         title = room_data['title'])
    #
    #     room_instance.save()
    #
    #     employee_instance = Employee.objects.create(**validated_data, account=user_instance)
    #     employee_instance.save(0)
    #     return employee_instance
    #

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
#
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
