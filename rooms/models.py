from django.db import models


class MeetingRoom(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return f'Meetings Room title :{self.title}'