from .models import Person, Employer, BankAccount, RentalHome
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('url', 'name', 'age', 'job_title', 'company')

class EmployerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employer
        fields = ('url', 'employer_name', 'employer_address')

class BankAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('url', 'person', 'bank_name')

class RentalHomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalHome
        fields = ('url', 'home_address', 'tentants')