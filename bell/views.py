
from django.shortcuts import render
from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bell.models import *
from bell.serializers import *
from rest_framework import generics


#city based filter
class CityFilter(filters.FilterSet):
    class Meta:
        model = City
        fields = ['id','name','image', 'lat','lng']

class CityList(generics.ListAPIView):
    model=City
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveAPIView):
    model=City
    queryset = City.objects.all()
    serializer_class = CitySerializer






#Restaurant filter
class RestraFilter(filters.FilterSet):
    class Meta:
        model = Restra
        fields = ['id','city','area','image','restra_name','lat','lng']





class RestraList(generics.ListCreateAPIView):
    model=Restra
    queryset = Restra.objects.all()
    serializer_class = RestraSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class=RestraFilter

class RestraDetail(generics.RetrieveUpdateDestroyAPIView):
    model=Restra
    queryset = Restra.objects.all()
    serializer_class = RestraSerializer




#Deal filter
class DealFilter(filters.FilterSet):
    class Meta:
        model = Deal
        fields = ['id','restra_name', 'content','val']


class DealList(generics.ListCreateAPIView):
    model=Deal
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    filter_class=DealFilter


class DealDetail(generics.RetrieveUpdateDestroyAPIView):
    model=Deal
    queryset = Deal.objects.all()
    serializer_class = DealSerializer