from django.shortcuts import render
from django.http import HttpResponse 
from .models import Contact

def main(request):
    cont = Contact.objects.all()
    for elem in cont:
        print(elem.message)
    return HttpResponse("Salom")

# Create your views here.
