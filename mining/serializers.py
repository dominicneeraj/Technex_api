from rest_framework import serializers
from mining.models import *

class SubjectSerializer(serializers.ModelSerializer):


    class Meta:
        model = Subject
        fields = ['id','name', 'image']
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id','subject','chapter_title')


class ContentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Content
        fields = ('id','chapter_title', 'content','image')