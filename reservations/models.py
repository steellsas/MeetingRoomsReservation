from django.db import models
from rooms.models import MeetingRoom
from employees.models import Employee

#
# class EmployeesInMeetingRoom(models.Model):
#     employee = models.ManyToManyField(Employee, blank=True)
#
#
# class MeetingRoomReservation(models.Model):
#     title = models.CharField(max_length=200)
#     from_date = models.DateField()
#     to_date = models.DateField()
#     room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
#     employees = models.ForeignKey(EmployeesInMeetingRoom, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.title}:from{self.from_date} to {self.to_date}'


class RoomBooking(models.Model):
    title = models.CharField(max_length=150)
    date_from = models.DateField()
    date_to = models.DateField()
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f' Title: {self.title}'
