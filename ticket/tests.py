from rest_framework.test import APITestCase, APIRequestFactory
from .models import Airplane, Ticket, Seat, Flight
from django.test import TestCase
from user.models import User
from .views import ticket_list

class TicketTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.flight = Flight.objects.create(
            flight_num='F267', 
            origin='Moscow',
            destination='Bishkek',
            departure_date='2020-12-23',
            departure_time='15:00:00',
            arrival_date='2020-12-23',
            arrival_time='21:00:00'
            )
        user = User.objects.create_user(
            email='alina@gmail.com', 
            password='1234',
            name='alina', 
            is_active=True)
        self.token = '12345'

        tickets = (
            Ticket(
                user=user,
                flight=self.flight,
                price='15000'
            ),
            Ticket(
                user=user,
                flight=self.flight,
                price='12000'
            )
        )
        Ticket.objects.bulk_create(tickets)


    def test_ticket_listing(self):
        request = self.factory.get('api/v1/ticket/')
        view = ticket_list
        response = view(request)

        assert response.status_code == 200

 


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




