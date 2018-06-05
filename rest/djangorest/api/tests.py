from django.test import TestCase

# Create your tests here.
from .models import Bucketlist
from rest_framework.test import APIClient
from  rest_framework import status
from django.urls import reverse

def ViewTestCase(TestCase):

    def setUp(self):
        self.client=APIClient()
        self.bucketlist_data = {'name':'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")


    def test_api_can_create_a_bucketlist(self):

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
