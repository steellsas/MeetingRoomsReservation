import factory

from rooms.models import MeetingRoom
from reservations.models import RoomBooking
from tests.factories.employee_model_factory import EmployeeFactory
from tests.factories.rooms_model_factory import MeetingRoomFactory


class RoomBookingFactory(factory.Factory):
    class Meta:
        model = RoomBooking
    id = factory.Sequence(lambda n: n+10)
    title = factory.Faker('sentence', nb_words=3)
    date_from = '2021-11-01'
    date_to = '2021-11-02'
    room = factory.SubFactory(MeetingRoomFactory)
    # start_date = factory.fuzzy.FuzzyDate()
    # end_date = factory.LazyAttribute(
    #     lambda o: o.start_date + datetime.timedelta(days=2 if o.duration == 'short' else 7)
    # )


    # @factory.post_generation
    # def employees(self, create, extracted, **kwargs):
    #     if not create:
    #         # Simple build, do nothing.
    #         return
    #     if extracted:
    #         # A list of groups were passed in, use them
    #         for employee in extracted:
    #             self.employees.add(employee)

    @classmethod
    def _prepare(cls, create, **kwargs):
        employee = EmployeeFactory()
        room_booking = super(RoomBookingFactory, cls)._prepare(create, **kwargs)
        room_booking.employees.add(employee)
        return room_booking
    

