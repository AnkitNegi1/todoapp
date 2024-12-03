from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import TodoData

class TaskAPITest(APITestCase):
    def setUp(self):
        self.task = TodoData.objects.create(
            todotitle="Sample Task",
            tododescription="Sample Description",
            tododate = '2024-12-30',
            todostatus="OPEN"
        )
        self.create_url = reverse('task-list-create')
        self.detail_url = reverse('task-detail', args=[self.task.id])

    def test_get_all_tasks(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data = {"todotitle": "New Task", "tododescription": "Description","tododate": '2025-01-01', "todostatus": "OPEN"}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        data = {"todotitle": "Updated Task", "tododescription": "Updated Description","tododate": '2025-01-31' , "todostatus": "WORKING"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
