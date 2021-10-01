from django.contrib import admin
from reservations.models import MeetingRoomReservation, EmployeesInMeetingRoom

admin.site.register(MeetingRoomReservation)
admin.site.register(EmployeesInMeetingRoom)