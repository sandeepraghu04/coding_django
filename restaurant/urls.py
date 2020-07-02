from django.urls import path
from .views import *

urlpatterns = [
    path('restaurant', submit_restaurant), # POST
    path('restaurants', get_restaurants), # GET
    path('restaurant/<int:pk>', modify_restaurant), # GET, PUT, DELETE
    path('restaurant/<int:pk>/rate', submit_rating), # POST
]
