
from django.shortcuts import render
from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mining.models import *
from mining.serializers import *
from rest_framework import generics

class ChapterList(generics.ListCreateAPIView):
    model=Chapter
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('subject','subject')
filter_fields = ('id')

class ChaptertDetail(generics.RetrieveUpdateDestroyAPIView):
    model=Chapter
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer




class SubjectList(generics.ListAPIView):
    model=Subject
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveAPIView):
    model=Subject
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ContentList(generics.ListCreateAPIView):
    model=Content
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('chapter_title','chapter_title')


class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    model=Content
    queryset = Content.objects.all()
    serializer_class = ContentSerializer