from rest_framework import serializers, viewsets
from .models import Airplane, Seat, Flight, Ticket
from datetime import datetime

class AirplaneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airplane
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'

    def validate(self, data):
        flight = data.get('flight')
        departure_datetime = datetime.combine(flight.departure_date, flight.departure_time)
        arrival_date  = data.get('arrival_date ')

        
        if arrival_date  is not None and arrival_date > departure_datetime:
            raise serializers.ValidationError('Билет невозможно приобрести после вылета рейса')
            
        return data
    
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    



class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = '__all__'


    def validate(self, data):
        airplane = data.get('airplane')
        row = data.get('row')
        seat_num = data.get('seat_num')

        if Seat.objects.filter(airplane=airplane, row=row, seat_num=seat_num).exists():
            raise serializers.ValidationError('Это место уже занято')
        
        return data


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = '__all__'

    
    def validate(self, data):
        flight_num = data.get('flight_num')
        
        if Flight.objects.filter(flight_num=flight_num).exists():
            raise serializers.ValidationError('Такой рейс уже существует')
        
        return data
    