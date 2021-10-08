import factory
from django.contrib.auth.models import User
from django.conf import settings
from employees.models import Employee


class UserFactory(factory.Factory):
    class Meta:
        model= User
    id = factory.Sequence(lambda n: n+1)
    username = "Firstuser"
    password = 'test12345'
    email = "trescias@mail.com"


class EmployeeFactory(factory.Factory):
    class Meta:
        model = Employee
    id = factory.Sequence(lambda n: n+10)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    account = factory.SubFactory(UserFactory)