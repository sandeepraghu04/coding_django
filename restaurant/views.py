from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Sum
from rest_framework.status import HTTP_200_OK
from .models import *
from .serializers import *


@api_view(['GET'])
def get_restaurants(request):
    restaurants = Restaurant.objects.all()
    res_serialized = RestaurantSerializer(restaurants, many=True)
    return Response(data=res_serialized.data, status=HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def modify_restaurant(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    msg = 'Restaurant Not Found'
    if restaurant:
        res_serialized = RestaurantSerializer(restaurant)
        if request.method == 'PUT':
            res_serialized = RestaurantSerializer(restaurant, data=request.data)
            if res_serialized.is_valid():
                res_serialized = res_serialized.save()
                msg = 'Restaurant Updated'
            else:
                msg = 'Restaurant Not Valid'
        elif request.method == 'GET':
            return Response(data=res_serialized.data, status=HTTP_200_OK)
        else:
            restaurant.delete()
            msg = 'Restaurant Deleted'
    return Response(data={'msg': msg}, status=HTTP_200_OK)

@api_view(['POST'])
def submit_restaurant(request):
    restaurant = request.data
    res_serialized = RestaurantSerializer(data=restaurant)
    if res_serialized.is_valid():
        res_serialized.save()
    return Response(data=res_serialized.data, status=HTTP_200_OK)

@api_view(['POST'])
def submit_rating(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    rating = request.data
    rating['res_id'] = pk
    print(rating)
    rat_serialized = RatingSerializer(data=rating)
    if rat_serialized.is_valid():
        rat_serialized.save()
        ratings = Rating.objects.filter(res_id=pk).count()
        total_rate = Rating.objects.aggregate(Sum('rate'))['rate__sum']
        avg_rating = total_rate / ratings
        rating['avg_rating'] = avg_rating
        res_ser = RestaurantSerializer(restaurant, data=rating)
        if res_ser.is_valid():
            res_ser.save()
    else:
        return Response(data={'msg': 'Please provide valid rating'}, status=HTTP_200_OK)
    return Response(data=rat_serialized.data, status=HTTP_200_OK)
