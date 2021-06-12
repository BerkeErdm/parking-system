from rest_framework import serializers
from carparks.models import CarParks

class CarParksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarParks
        fields = {
            'parkName',
            'districtName',
            'address',
            'openUntil',
            'image',
            'slug',
            'phone',
            'latitude',
            'longitude',
        }

        model = CarParks
        fields = '__all__'
