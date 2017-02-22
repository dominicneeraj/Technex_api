from rest_framework import serializers
from menu.models import *


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('subject','image')
