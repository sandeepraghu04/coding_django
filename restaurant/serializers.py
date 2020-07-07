from django.db import models
from .models import *
from rest_framework.serializers import ModelSerializer, ValidationError


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

    def validate(self,data):
        errors = {}
        if not data.get('name'):
            errors['name'] = 'please provide name field'
        if data.get('name') and len(data.get('name')) <= 3:
            errors['name'] = 'please provide a valid name, Name suppost to be more than 2 chars'
        if errors:
            raise ValidationError(errors)
        return data


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

    def validate(self,data):
        rate = data.get('rate')
        if not rate or rate < 0 or rate > 5:
            raise ValidationError('Please provide valid rate')
        return data
