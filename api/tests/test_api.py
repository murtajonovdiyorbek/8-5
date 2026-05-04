import json

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from telebot.util import content_type_service
from yaml import serialize

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



    def test_get_filter(self):
        url = reverse('category-list')

        self.client.force_login(self.user)
        response = self.client.get(url, data={'description': 'salom'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.json())


    def test_get_search(self):
        url = reverse('category-list')

        self.client.force_login(self.user)
        response = self.client.get(url, data={'search': 'badiy'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = CategorySerializer([self.category1, self.category2], many=True)

        self.assertEqual(response.json(), serializer.data)


    def test_get_ordering(self):
        url = reverse('category-list')

        self.client.force_login(self.user)
        response = self.client.get(url, data={'ordering': 'name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = CategorySerializer([self.category1, self.category2], many=True)

        self.assertEqual(response.json(), serializer.data)


    def test_create(self):
        url = reverse('category-list')

        data = {
            'name': 'Dm',
            'description': 'salom'
        }

        self.client.force_login(self.user)
        response = self.client.get(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Category.objects.all().count(), 4)


    def test_update(self):
        url = reverse('category-list')

        data = {
            'name': self.category1.name,
            'description': 'salom'
        }

        self.client.force_login(self.user)
        response = self.client.get(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.category1.refresh_from_db()
        self.assertEqual(self.category1.description, 5)

    def test_partial_update(self):
        url = reverse('category-list')

        data = {
            'description': 'salomm'
        }

        self.client.force_login(self.user)
        response = self.client.patch(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.category1.refresh_from_db()
        self.assertEqual(self.category1.description, 5)
