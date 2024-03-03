from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import date
from flights.models import Flight, SearchFlight, SearchFlightResult
import json


class FlightViewsTestCase(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.client = Client()

        self.flight = Flight.objects.create(
            flight_number='ABC123',
            airline_name='Mock Airlines',
            departure_time=timezone.now(),
            arrival_time=timezone.now(),
            duration='2 hours',
            no_of_stops=1,
            price=200
        )

        self.search_flight = SearchFlight.objects.create(
            source_city='Source City',
            destination_city='Destination City',
            travel_date=date.today()
        )

        self.search_flight_result = SearchFlightResult.objects.create(
            flight=self.flight,
            search_request=self.search_flight,
            total_results=1
        )

    def test_flight_list_view(self):
        response = self.client.get(reverse('flight_list'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['flight_number'], 'ABC123')

    def test_search_flights_view(self):
        url = reverse('search_flights')
        data = {
            'sourceCity': 'Source City',
            'destinationCity': 'Destination City',
            'travelDate': str(date.today()),
            'returnDate': str(date.today())
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['flight_number'], 'ABC123')
