from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def welcome(request):

    return Response("welcome to apis")

@api_view(['POST'])
def postmethod(request):
    
    return Response("This is post method")

@api_view(['GET','POST'])
def getorpost(request):

    if request.method =="POST":
        return Response("This is post method,let's post something...")
    
    if request.method =="GET":
        return Response("this is get method,let's get some data from db...")
    
    else:
        return Response ("This is other ---",request.method)