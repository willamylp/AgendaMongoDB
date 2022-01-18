from django.test import TestCase
from Apps.Usuario.forms import UserAutenticationForm

class UsuarioFormTestCase(TestCase):

    def test_when_user_informs_only_username_and_empty_pass(self):
        form = UserAutenticationForm(data={})
        self.assertFalse(form.is_valid())
    