from django.db import models
from rooms.models import MeetingRoom
from employees.models import Employee


class EmployeesInMeetingRoom(models.Model):
    employee = models.ManyToManyField(Employee)


class MeetingRoomReservation(models.Model):
    title = models.CharField(max_length=200)
    from_date = models.DateField()
    to_date = models.DateField()
    room = models.ManyToManyField(MeetingRoom)
    employees = models.ForeignKey(EmployeesInMeetingRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f'{title}:from{self.from_date} to {self.to_date}'