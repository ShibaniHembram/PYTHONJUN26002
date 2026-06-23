from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home/index.html")

def add(request):
    return render(request, "add/index.html")