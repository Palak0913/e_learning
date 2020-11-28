from django.shortcuts import render

from .models import Course, Subject
from .serializers import CourseSerializer, SubjectSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated



class CreateSubjectAPI(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CourseListAPI(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


#class CourseDetailView():



class CreateCourseAPI(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# Create your views here.
