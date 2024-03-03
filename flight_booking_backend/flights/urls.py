from django.urls import path
from .views import flight_list, search_flights

urlpatterns = [
    path('', flight_list, name='flight_list'),
    path('search/', search_flights, name='search_flights'),
]