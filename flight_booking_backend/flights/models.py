from django.db import models

# Create your models here.


class Flight(models.Model):
    flight_number = models.CharField(max_length=50)
    airline_name = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.CharField(max_length=50)
    no_of_stops = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.airline_name} - {self.flight_number}"


class SearchFlight(models.Model):
    source_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    travel_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.source_city} to {self.destination_city} on {self.travel_date}"


class SearchFlightResult(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    search_request = models.ForeignKey(SearchFlight, on_delete=models.CASCADE)
    total_results = models.IntegerField(default=0)

    def __str__(self):
        return f"Flight Search Result for {self.search_request}"