from rest_framework.test import APITestCase, APIRequestFactory
from .models import Airplane, Ticket, Seat, Flight
from django.test import TestCase


class FlightModelTestCase(TestCase):

    def test_flight_create(self):
        flight = Flight.objects.create(
            flight_num = 'F123',
            origin = 'New York',
            destination = 'Los Angeles',
            departure_date = '2023-09-01',
            departure_time = '10:00:00',
            arrival_date = '2023-09-01',
            arrival_time = '12:00:00'
        )
        assert flight.flight_num == "F123"
        


class AirplaneModelTestCase(TestCase):

    def test_airplane_create(self):
        airplane = Airplane.objects.create(
            air_name = 'AirBus',
            model_air = 'boeing',
            seats = 2
        )
        assert airplane.air_name == 'AirBus'
        assert airplane.seats == 2
