from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
     
     person = {
         'name' : 'John',
         'age' : 40,
         'Place': 'Calicut'
       }
     return render(request, 'index.html', person)

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')