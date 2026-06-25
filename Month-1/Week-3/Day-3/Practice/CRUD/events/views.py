from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event
from django.core.paginator import Paginator

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

@api_view(['GET'])
def getEventByID(request,id):
    try:
        event = Event.objects.get(id=id)
        serData = EventSerializer(event)

        return Response({
            "data":serData.data,
            "message":"Event fetch susscfully"
        })
    
    except Event.DoesNotExist:
        return Response({
            "data":[],
            "message":"Event not found"
        })
    
@api_view(['PUT'])
def updateEvent(request,id):
    try:
        event = Event.objects.get(id=id)
        
    except Event.DoesNotExist:
        return Response({
            "message":"Event not found"
        })
    
    serData = EventSerializer(event, data=request.data, partial=True)

    if (serData.is_valid()):
        serData.save()

        return Response({
            "message":"Event update successfully",
            "event":serData.data
        })

    return Response({
        "message":"Event not update",
        "errors":serData.errors
        })

@api_view(['DELETE'])
def deleteEvent(request,id):
    try:
        event = Event.objects.get(id=id)
        
    except Event.DoesNotExist:
        return Response({
            "message":"Event not found"
        })
    
    event.delete()

    return Response({
        "message":"Event deleted successfully",
    })

@api_view(['GET'])
def getEventByPaginate(request):
    page = int(request.GET.get('page',1))
    per_page = int(request.GET.get('per_page',2))

    events = Event.objects.all()

    paginator = Paginator(events,per_page)
    page_obj = paginator.get_page(page)

    serData = EventSerializer(page_obj.object_list,many=True)

    return Response({
       "Events":serData.data,
       "pagination":{
           "current_page":page_obj.number,
           "per_page":per_page,
           "total":paginator.count,
           "last_page":paginator.num_pages,
           "has_next_page":page_obj.has_next(),
           "has_previous_page":page_obj.has_previous()
       }
    })