from django.apps import AppConfig


class FlightsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flights'

    def ready(self):
        # from .models import Flight
        # if Flight.objects.exists():
        #     return  # If data exists, do not populate

        from .populate_flights import populate_flights
        populate_flights()
