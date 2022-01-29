from Apps.Compartilhado import views
from django.test import TestCase
from django.urls import resolve, reverse


class CompartilhadoTestViews(TestCase):

    def test_urls_create_share_exists(self):
        resolver = resolve('/compartilhado/newshared/1/')
        self.assertEqual(resolver.url_name, 'create_share')

    def test_urls_list_share_exists(self):
        resolver = resolve('/compartilhado/listshare/')
        self.assertEqual(resolver.url_name, 'list_share')

    def test_template_used_to_render_the_listshare(self):
        response = self.client.get(reverse('list_share'))
        self.assertTemplateUsed(
            response, 'Compartilhado/compartilhados_list.html')

    def test_view_func_based_call_is(self):
        view = resolve(reverse('create_user'))
        self.assertNotIsInstance(view.func, views.ListShare)
