from django.urls import path
from .views import *

urlpatterns = [
    # path('main', main),
    path('gallery/', Create_gal),
    path('consultation', Create_cons)

]