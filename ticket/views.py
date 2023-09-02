from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Ticket, Airplane, Seat, Flight
from .serializers import TicketSerializer, FlightSerializer, SeatSerializer, AirplaneSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



@api_view(['GET', 'POST'])
def ticket_list(request):
    if request.method == 'GET':
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=200)
    
    
@api_view(['PATCH'])
def update_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    serializer = TicketSerializer(ticket, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Билет успешно обновлен', status=201)
    
    
@api_view(['DELETE'])
def delete_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    ticket.delete()
    return Response('Билет успешно удален', status=204)
    


@api_view(['GET', 'POST'])
def flight_list(request):
    if request.method == 'GET':
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
@api_view(['PATCH'])
def update_flight(request, id):
    flight = get_object_or_404(Flight, id=id)
    serializer = FlightSerializer(flight, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Рейс успешно обновлен', status=201)
    


@api_view(['DELETE'])
def delete_flight(request, id):
    flight = get_object_or_404(Flight, id=id)
    flight.delete()
    return Response('Рейс успешно удален', status=204)
    


@api_view(['GET', 'POST'])
def seat_list(request):
    if request.method == 'GET':
        seats = Seat.objects.all()
        serializer = SeatSerializer(seats, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['PATCH'])
def update_seat(request, id):
    seat = get_object_or_404(Seat, id=id)
    serializer = SeatSerializer(seat, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Место успешно обновлено', status=201)


@api_view(['DELETE'])
def delete_seat(request, id):
    seat = get_object_or_404(Seat, id=id)
    seat.delete()
    return Response('Место успешно удалено', status=204)
    

@api_view(['GET', 'POST'])
def airplane_list(request):
    if request.method == 'GET':
        airplane = Airplane.objects.all()
        serializer = AirplaneSerializer(airplane, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AirplaneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['PATCH'])
def update_airplane(request, id):
    airplane = get_object_or_404(Airplane, id=id)
    serializer = AirplaneSerializer(airplane, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Самолет успешно обновлен', status=201)
    

@api_view(['DELETE'])
def delete_airplane(request, id):
    airplane = get_object_or_404(Airplane, id=id)
    airplane.delete()
    return Response('Самолет успешно удален', status=204)