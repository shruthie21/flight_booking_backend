from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Flight
# from .serializers import FlightSerializer


@csrf_exempt
def flight_list(request):
    """
       Retrieves a list of flights.
       Response: Details of a flight including flight number, airline name, departure time,
           arrival time, duration, number of stops, price, source city, and destination city.
    """
    if request.method == 'GET':
        flights = Flight.objects.all()
        data = []
        for flight in flights:
            search_flight_result = flight.searchflightresult_set.first()
            if search_flight_result:
                search_request = search_flight_result.search_request
                source_city = search_request.source_city
                destination_city = search_request.destination_city
            else:
                source_city = None
                destination_city = None

            flight_data = {
                'flight_number': flight.flight_number,
                'airline_name': flight.airline_name,
                'departure_time': flight.departure_time,
                'arrival_time': flight.arrival_time,
                'duration': flight.duration,
                'no_of_stops': flight.no_of_stops,
                'price': flight.price,
                'source_city': source_city,
                'destination_city': destination_city
            }
            data.append(flight_data)

        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def search_flights(request):
    """
        Searches for flights based on given sourceCity and destinationCity.
        Returns: JsonResponse: A JSON response containing the list of flights matching the search criteria.
    """
    if request.method == 'POST':
        source_city = request.POST.get('sourceCity')
        destination_city = request.POST.get('destinationCity')
        travel_date = request.POST.get('travelDate')
        return_date = request.POST.get('returnDate')

        # Filter flights based on search criteria
        flights = Flight.objects.filter(
            Q(searchflightresult__search_request__source_city__iexact=source_city) &
            Q(searchflightresult__search_request__destination_city__iexact=destination_city))
        print(f'flights: {flights}')

        data = [{'flight_number': flight.flight_number,
                 'airline_name': flight.airline_name,
                 'departure_time': flight.departure_time,
                 'arrival_time': flight.arrival_time,
                 'duration': flight.duration,
                 'no_of_stops': flight.no_of_stops,
                 'price': flight.price,
                 'source_city': source_city,
                 'destination_city': destination_city,
                 'travel_date': travel_date,
                 'return_date': return_date
                 } for flight in flights]
        print(f'Flight Data: {data}')
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

# class SearchFlightsAPIView(APIView):
#     """
#     Searches for flights based on given sourceCity and destinationCity.
#     """
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, *args, **kwargs):
#         return super(SearchFlightsAPIView, self).dispatch(*args, **kwargs)
#
#     @csrf_exempt
#     def post(self, request):
#         source_city = request.data.get('sourceCity')
#         destination_city = request.data.get('destinationCity')
#         travel_date = request.data.get('travelDate')
#         return_date = request.data.get('returnDate')
#
#         print('sourcecity-----', source_city)
#         print('destination cirty-------', destination_city)
#
#         # Filter flights based on search criteria
#         flights = Flight.objects.filter(
#             Q(searchflightresult__search_request__source_city__iexact=source_city) &
#             Q(searchflightresult__search_request__destination_city__iexact=destination_city))
#
#         data = [{'flight_number': flight.flight_number,
#                  'airline_name': flight.airline_name,
#                  'departure_time': flight.departure_time,
#                  'arrival_time': flight.arrival_time,
#                  'duration': flight.duration,
#                  'no_of_stops': flight.no_of_stops,
#                  'price': flight.price,
#                  'source_city': source_city,
#                  'destination_city': destination_city,
#                  'travel_date': travel_date,
#                  'return_date': return_date
#                  } for flight in flights]
#
#         return Response(data)
#
#     def get(self, request):
#         return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

