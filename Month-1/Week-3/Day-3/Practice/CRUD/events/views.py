from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event

# Create your views here.
@api_view(['GET'])
def welcome(request):
    return Response("welcome to events apis...")

@api_view(['POST'])
def addevent(request):

    serializer = EventSerializer(data=request.data)

    if (serializer.is_valid()):
        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serData = EventSerializer(events,many=True)

    return Response(serData.data)