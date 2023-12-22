from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    text = "Salom user"
    return render(request, "index.html", {"data":text})

def dashboard(request):
    text = "Dashboard"
    return render(request, "index.html", {"data":text})

# Create your views here.
