from django.db import models
from rooms.models import MeetingRoom
from employees.models import Employee


class RoomBooking(models.Model):
    title = models.CharField(max_length=150)
    date_from = models.DateField()
    date_to = models.DateField()
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    employees = models.ManyToManyField(Employee, blank=True)


    def __str__(self):
        return f' Title: {self.title}'
