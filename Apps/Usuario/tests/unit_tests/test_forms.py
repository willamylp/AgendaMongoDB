from django.test import TestCase
from Apps.Usuario.forms import UserAutenticationForm, UserCreationForms
from django.forms import ValidationError

class UsuarioFormTestCase(TestCase):

    def test_when_user_informs_only_username_and_empty_pass(self):
        form = UserAutenticationForm(data={})
        self.assertFalse(form.is_valid())

    # def test_validate(self):
    #     data_forg={"username":"unao","first_name":"Bruno","last_name":"Ferreira","password1":"ygfy4545#fhh","password2":"ygfy4545#fhh","email":"uno@gmail.com"}
    #     self.userform = UserCreationForms(data_forg)
    #     self.userform.username = 499 * 'B'
    #     with self.assertRaises(ValidationError):
    #         self.userform.full_clean()
    