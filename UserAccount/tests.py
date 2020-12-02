import json

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import RegisterSerializer, UserSerializer
from .views import RegisterAPI

User=get_user_model()

class Test_Register(APITestCase):

    def test_registration(self):
        data = {
            "username": "xyz",
            "email": "xyz@gmail.com",
            "password": "xyz123"
        }
        response = self.client.post("api/register/", data )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create your tests here.
