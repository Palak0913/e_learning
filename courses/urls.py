from .views import CourseListAPI,CreateCourseAPI,CreateSubjectAPI
from django.urls import path

urlpatterns = [
    path('courseList/', CourseListAPI.as_view(), name='Course-list'),
    path('createCourse/', CreateCourseAPI.as_view(), name='create-Course'),
    path('createSubject/', CreateSubjectAPI.as_view(), name='create-Subject'),
    
    
]