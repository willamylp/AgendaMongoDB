from Apps.Usuario import views
from django.test import TestCase
from django.urls import resolve, reverse


class UsuarioTestViews(TestCase):

    """resolve() retorna um objeto da classe  ResolverMatch, que tem varios
    metodos de acesso, se não tiver retorna uma except http404 """

    def test_urls_exists(self):
        resolver = resolve('/new/')
        self.assertEqual(resolver.url_name, 'create_user')

    def test_template_used_to_render_the_view_create(self):
        response = self.client.get(reverse('create_user'))
        self.assertTemplateUsed(response, 'create.html')

    def test_view_func_based_call_is(self):
        view = resolve(reverse('create_user'))
        self.assertIs(view.func, views.create_user)

    def test_view_loginUser_home_status_code_200(self):
        response = self.client.get(reverse('loginUser_home'))
        self.assertEqual(response.status_code, 200)

    def test_template_used_to_render_the_view(self):
        response = self.client.get(reverse('loginUser_home'))
        self.assertTemplateUsed(response, 'index.html')

    def test_when_calling_the_view_without_authenticating_if_it_is_redirected(
            self):
        response = self.client.get(reverse('ListarContato'))
        self.assertEqual(response.status_code, 302)
