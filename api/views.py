from django.shortcuts import render, get_object_or_404, redirect
from multiprocessing import context
from django.http import HttpResponse, Http404
from .models import Person, Employer, BankAccount, RentalHome
from . serializers import PersonSerializer, EmployerSerializer, BankAccountSerializer, RentalHomeSerializer
from rest_framework import status, permissions, viewsets



from rest_framework.response import Response
from rest_framework.decorators import action


class PersonViewSet(viewsets.ModelViewSet):
    """
    All the 'persons' entered into the application and there jobs
    """
    # These dont really do anything (unless passed as a parameter to one of the methods)
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()

    
class EmployerViewSet(viewsets.ModelViewSet):
    """
    All the employers entered into the application 
    """
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

    def get_queryset(self):
        return Employer.objects.all()


class BankAccountViewSet(viewsets.ModelViewSet):
    """
    All the bank accounts
    """
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

    def get_queryset(self):
        return BankAccount.objects.all()


class RentalHomeViewSet(viewsets.ModelViewSet):
    """
    All the home being rented along with the tenants living in them
    """
    queryset = RentalHome.objects.all()
    serializer_class = RentalHomeSerializer
    
    def get_queryset(self):
        return RentalHome.objects.all()