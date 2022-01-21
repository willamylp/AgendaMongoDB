from Apps.Usuario.forms import UserAutenticationForm
from django.test import TestCase


class UsuarioFormTestCase(TestCase):

    def test_when_user_informs_only_username_and_empty_pass(self):
        form = UserAutenticationForm(data={})
        self.assertFalse(form.is_valid())
