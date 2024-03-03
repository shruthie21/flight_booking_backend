import json
from datetime import datetime
from .models import Flight, SearchFlight, SearchFlightResult


def delete_existing_data():
    Flight.objects.all().delete()
    SearchFlight.objects.all().delete()
    SearchFlightResult.objects.all().delete()


def populate_flights():
    with open('flights/flights_records_json/flights.json') as f:
        flights_data = json.load(f)

    for flight_data in flights_data:
        flight = Flight.objects.create(
            flight_number=flight_data['flight_number'],
            airline_name=flight_data['airline_name'],
            departure_time=datetime.fromisoformat(flight_data['departure_time']),
            arrival_time=datetime.fromisoformat(flight_data['arrival_time']),
            duration=flight_data['duration'],
            no_of_stops=flight_data['no_of_stops'],
            price=flight_data['price']
        )

        search_flight = SearchFlight.objects.create(
            source_city=flight_data['source_city'],
            destination_city=flight_data['destination_city'],
            travel_date=datetime.fromisoformat(flight_data['departure_time']),
            return_date=datetime.fromisoformat(flight_data['arrival_time']) if 'arrival_time' in flight_data else None
        )

        SearchFlightResult.objects.create(
            flight=flight,
            search_request=search_flight,
            total_results=1
        )


if not Flight.objects.exists():
    populate_flights()
