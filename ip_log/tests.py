from rest_framework import status
from rest_framework.test import APITestCase

from .models import LogEntry


class TestIpLogView(APITestCase):

    def test_get(self):
        request = self.client.get('/ip/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_post(self):
        request = self.client.post('/ip/')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LogEntry.objects.count(), 1)
