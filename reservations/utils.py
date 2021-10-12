from reservations.models import RoomBooking
from django.utils.timezone import datetime


def check_date_in_reservations_availability(date):

    date_is_used = False
    if RoomBooking.objects.filter(date_from__lte=date,date_to__gte=date):
        date_is_used =True

    return date_is_used






