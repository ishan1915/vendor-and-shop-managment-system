
# Create your tests here.

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Vendor, Shop

class VendorShopAPITestCase(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create_user(username='vendor1', password='password123', business_name='ShopOne')
        self.shop_data = {
            'name': 'Test Shop',
            'business_type': 'Grocery',
            'latitude': 12.9716,
            'longitude': 77.5946
        }

    def authenticate(self):
        response = self.client.post(reverse('token_obtain_pair'), {'username': 'vendor1', 'password': 'password123'})
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")

    def test_register_vendor(self):
        response = self.client.post(reverse('register_vendor'), {
            'username': 'vendor2',
            'password': 'password123',
            'business_name': 'ShopTwo'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_shop(self):
        self.authenticate()
        response = self.client.post(reverse('shop_list_create'), self.shop_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_nearby_shops(self):
        self.authenticate()
        self.client.post(reverse('shop_list_create'), self.shop_data)
        response = self.client.get(reverse('nearby_shops'), {'latitude': 12.97, 'longitude': 77.59, 'radius': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

