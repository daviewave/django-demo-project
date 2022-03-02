from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class Employer(models.Model):
    employer_name = models.CharField(max_length=256, null=True)
    employer_address = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.employer_name


class Person(models.Model):
    name = models.CharField(max_length=256, null=True)
    age = models.IntegerField(default=18, null=True)
    social_security = models.CharField(max_length=9, null=True)
    job_title = models.CharField(max_length=256, null=True)
    company = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} || {self.job_title}"


class BankAccount(models.Model):
    account_number = models.CharField(max_length=10, null=True)
    bank_name = models.CharField(max_length=256, null=True)
    bank_address = models.CharField(max_length=256, null=True)
    bank_routing = models.CharField(max_length=8, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.bank_name} || {self.person}"


class RentalHome(models.Model):
    home_address = models.CharField(max_length=256, null=True)
    current_price = models.CharField(max_length=256, null=True)
    rent_amount = models.CharField(max_length=256, null=True)
    tentants = models.ManyToManyField(Person)

    def __str__(self):
        return self.home_address

