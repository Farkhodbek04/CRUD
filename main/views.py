from django.shortcuts import render
from django.http import HttpResponse 
from .models import Contact, Gallery, Testimonals, Consultation


# CRUD => Create, Read, Update, Delete

# def main(request):
#     cont = Contact.objects.all()
#     for elem in cont:
#         print(elem.message)
#     return HttpResponse("Salom")

## Let' create CRUDs here!

# Gallery
def Create_gal(request):
    icon = Gallery.objects.create(icon="7.jpg")
    description = Gallery.objects.create(description="Description has been created!")
    return HttpResponse(" New Gallery has been created here! ")

def read_gal(request):
    icon = Gallery.objects.all()
    description = Gallery.objects.all()
    return HttpResponse(" gallery has been read!")

def update_gal(request):
    icon = Gallery.objects.get(id=1)
    icon.description = " Description has just been updated! "
    icon.save()
    return HttpResponse("Updated!")

def del_gal(request):
    icon = Gallery.objects.get(id=1)
    icon.delete()
    return HttpResponse(" Gallery has been deleted! ")

    # Consultation
def Create_cons(request):
    name = Consultation.objects.create(name="Jack")
    email = Consultation.objects.create(email="email has been created!")
    phone = Consultation.objects.create(phone="phone has been created!")
    return HttpResponse(" New Consultation has been created here! ")

def read_cons(request):
    name = Consultation.objects.all()
    email =Consultation.objects.all()
    phone = Consultation.objects.all()
    return HttpResponse(" Consultation has been read!")

def update_consu(request):
    name = Consultation.objects.get(id=1)
    name.description = " Consultation has just been updated! "
    name.save()
    return HttpResponse("Updated!")

def del_consu(request):
    email = Consultation.objects.get(id=1)
    email.delete()
    return HttpResponse(" Consultation has been deleted! ")

# Testimonals

def Create_test(request):
    icon = Testimonals.objects.create(icon="7.jpg")
    title = Testimonals.objects.create(title="title has been created!")
    body = Testimonals.objects.create(body="body has been created!")
    return HttpResponse(" New Testimonals has been created here! ")

def read_test(request):
    icon = Testimonals.objects.all()
    title = Testimonals.objects.all()
    body = Testimonals.objects.all()
    return HttpResponse(" Testimonal has been read!")

def update_test(request):
    title = Testimonals.objects.get(id=1)
    title.description = " Tile has just been updated! "
    title.save()
    return HttpResponse("Updated!")

def del_test(request):
    body = Testimonals.objects.get(id=1)
    body.delete()
    return HttpResponse(" Body has been deleted! ")

# Contact

def Create_cont(request):
    name = Contact.objects.create(name="Bruce")
    email = Contact.objects.create(email="email has been created!")
    message = Contact.objects.create(message="message has been created!")
    return HttpResponse(" New Contact has been created here! ")

def read_cont(request):
    name = Contact.objects.all()
    email =Contact.objects.all()
    message = Contact.objects.all()
    return HttpResponse(" Contact has been read!")

def update_cont(request):
    name = Contact.objects.get(id=1)
    name.description = " Contact has just been updated! "
    name.save()
    return HttpResponse("Updated!")

def del_cont(request):
    email = Consultation.objects.get(id=1)
    email.delete()
    return HttpResponse(" Contact has been deleted! ")