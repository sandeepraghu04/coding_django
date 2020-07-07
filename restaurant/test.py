import json
from unittest.mock import patch, Mock
from django.test import Client, TestCase


class TestRestaurant(TestCase):

    def setUp(self):
        self.data = {'name': 'What ever', 'desc': 'What ever',
                     'addr': 'Whatever', 'avg_rating': 4.9}
        res = self.client.post('/api/restaurant', self. data)
        self.base_url = '/api/restaurant'
        self.update_url = self.base_url + '/' + str(res.data['id'])
        self.rate_url = self.update_url + '/rate'

    def test_should_return_all_available_restaurants_from_db(self):
        res = self.client.get(self.base_url + 's', None)
        self.assertEqual(res.status_code, 200)

    def test_should_create_restaurant(self):
        res = self.client.post(self.base_url, self.data)
        self.assertEqual(res.status_code, 201)

    def test_should_update_restaurant(self):
        update_data = self.data
        update_data['avg_rating'] = 2.0
        res = self.client.put(self.update_url, update_data,
                              content_type='application/json')

        self.assertEqual(res.status_code, 200)

    def test_should_delete_restaurant(self):
        res = self.client.delete(self.update_url)
        self.assertEqual(res.status_code, 200)
