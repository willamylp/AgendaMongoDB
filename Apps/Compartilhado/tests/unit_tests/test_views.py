from django.test import TestCase
from django.urls import resolve


class CompartilhadoTestViews(TestCase):

    def test_urls_exists(self):
        resolver = resolve('/compartilhado/newshared/1/')
        self.assertEqual(resolver.url_name, 'create_share')
