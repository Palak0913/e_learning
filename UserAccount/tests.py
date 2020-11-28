import json

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User=get_user_model()

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "username": "xyz",
            "email": "xyz@gmail.com",
            "password": "xyz123"
        }
        response = self.client.post("api/register/", data )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Create your tests here.
