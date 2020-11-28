from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login
from .serializers import UserSerializer, RegisterSerializer,LoginUserSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import get_user_model
User = get_user_model()
"""

from courses.models import Course
from django.views.generic.detail import DetailView


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



#class StudentEnrollCourseView


#StudentCourseListView

#StudentCourseDetailView

###############################

#class RequestAPI():

"""
class ListUsers(APIView):
    
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    
    authentication_classes = [TokenAuthentication.authenticate]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        
        Return a list of all users.
        
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
"""