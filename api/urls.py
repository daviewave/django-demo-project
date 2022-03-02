from django.urls import path, include
from rest_framework import routers
from api import views
from django.conf import settings


# create the router and store it in a router variable
router = routers.DefaultRouter()

# Register the router with each viewset create
# In quanta source code they register each class AS A REGULAR EXPRESSION 
# then call the modalViewSet its being registered too
router.register(r'people', views.PersonViewSet, basename='person')
router.register(r'employers', views.EmployerViewSet, basename='employer')
router.register(r'bank_accounts', views.BankAccountViewSet, basename='bankaccount')
router.register(r'rental_homes', views.RentalHomeViewSet, basename='rentalhome')

urlpatterns = [
    path('', include(router.urls)),
]
