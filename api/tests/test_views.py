from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class BookViewTest(APITestCase):
    
    def test_response_is_correct(self):
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['hello'] == 'django'

class HealthViewTest(APITestCase):
    
    def test_response_is_correct(self):
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['status'] == 'ok'