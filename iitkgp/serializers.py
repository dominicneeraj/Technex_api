from rest_framework import serializers
from iitkgp.models import *


class DepartmentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Department
        fields = ['id','name', 'image']


class SubjectSerializer(serializers.ModelSerializer):


    class Meta:
        model = Subject
        fields = ['id','department','name', 'image']
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id','subject','chapter_title']


class ContentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Content
        fields = ['id','chapter_title', 'content','image']