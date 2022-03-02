from django.contrib import admin
from .models import Employer, Person, RentalHome, BankAccount

# Register your models here.
admin.site.register(Employer)
admin.site.register(Person)
admin.site.register(RentalHome)
admin.site.register(BankAccount)
