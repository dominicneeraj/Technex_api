from rest_framework import serializers
from bell.models import *


class CitySerializer(serializers.ModelSerializer):


    class Meta:
        model = City
        fields = ['id','name','image', 'lat','lng']


class RestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restra
        fields = ['id','city','area','image','restra_name','lat','lng']


class DealSerializer(serializers.ModelSerializer):


    class Meta:
        model = Deal
        fields = ['id','restra_name', 'content','val']