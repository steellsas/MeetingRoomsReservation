from rest_framework import serializers
from django.contrib.auth.models import User
from employees.models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        write_only_fields = ('password',)


class EmployeeSerializer1(serializers.ModelSerializer):
    account = UserSerializer()

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'account')

    def create(self, validated_data):
        user_data = validated_data.pop('account')
        user_instance = User.objects.create(
            username=user_data['username'],
            password=user_data['password'],
            email=user_data['email'])
        user_instance.save()
        employee_instance = Employee.objects.create(**validated_data, account=user_instance)
        employee_instance.save(0)
        return employee_instance


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','first_name', 'last_name', 'account')
