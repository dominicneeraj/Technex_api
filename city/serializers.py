from rest_framework import serializers
from city.models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
