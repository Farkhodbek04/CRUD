from django.db import models

# Create your models here.
class Gallery(models.Model):
    icon = models.ImageField()
    description = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = "Galareya"


class Consultation(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    phone = models.CharField(max_length = 13)

    class Meta:
        verbose_name_plural = "Konsultatsiya"

class Testimonals(models.Model):
    icon = models.ImageField()
    title = models.CharField(max_length = 255)
    body = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = "Mijozlar"

class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    message = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = "Bog'glanish"
        

