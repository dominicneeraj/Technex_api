
from django.shortcuts import render
from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mining.models import *
from iitkgp.serializers import *
from rest_framework import generics


class DepartmentList(generics.ListAPIView):
    model=Department
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveAPIView):
    model=Department
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class SubjectFilter(filters.FilterSet):
    class Meta:
        model = Subject
        fields = ['id','department','name', 'image']

class SubjectList(generics.ListAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class=SubjectFilter

class SubjectDetail(generics.RetrieveAPIView):
    model=Subject
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

#chapter filter
class ChapterFilter(filters.FilterSet):
    class Meta:
        model = Chapter
        fields = ['id','subject','chapter_title']





class ChapterList(generics.ListCreateAPIView):
    model=Chapter
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class=ChapterFilter

class ChaptertDetail(generics.RetrieveUpdateDestroyAPIView):
    model=Chapter
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer




#content filter
class ContentFilter(filters.FilterSet):
    class Meta:
        model = Content
        fields = ['id','chapter_title', 'content','image']


class ContentList(generics.ListCreateAPIView):
    model=Content
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_class=ContentFilter


class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    model=Content
    queryset = Content.objects.all()
    serializer_class = ContentSerializer