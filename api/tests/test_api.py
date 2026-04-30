from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import Category
from api.serializers import CategorySerializer

class CategoryTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='toxir', password='123')
        self.category1 = Category.objects.create(name='Badiy')
        self.category2 = Category.objects.create(name='Ilmiy')
        self.category3 = Category.objects.create(name='Diniy')

    def test_is_not_authenticated(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get(self):
        url = reverse('category-list')

        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = CategorySerializer([self.category1, self.category2, self.category3], many=True)
        self.assertEqual(response.json(), serializer.data)


    def test_one(self):
        url = reverse('category-detail', args=[self.category1.id])
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        serializer = CategorySerializer(self.category1)
        self.assertEqual(response.json(), serializer.data)