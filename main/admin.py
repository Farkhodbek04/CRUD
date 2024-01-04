from django.contrib import admin
from .models import Gallery, Contact, Consultation, Testimonals

class GalleryAdmin(admin.ModelAdmin):
    list_display = ("icon", "description")
admin.site.register(Gallery, GalleryAdmin)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
admin.site.register(Consultation, ConsultationAdmin)
class TestimonalsAdmin(admin.ModelAdmin):
    list_display = ("icon", "title", "body")
admin.site.register(Testimonals, TestimonalsAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")
admin.site.register(Contact, ContactAdmin)

# Register your models here.
