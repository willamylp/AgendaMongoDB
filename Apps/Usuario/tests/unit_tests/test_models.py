from typing import Final

from Apps.Usuario.forms import UserCreationForms
from Apps.Usuario.models import User
# Create your tests here.
from django.test import TestCase

PW: Final = "ygfy4545#fhh"


class UsuarioTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='Magaly', first_name='Julia',
                            last_name='Ferreira', password=PW,
                            email='Julia@gmail.com', bio='qualquer',
                            is_staff=False, is_active=False)

    def test_user_created_is_saved(self):
        data_forg = {"username": "Bruno", "first_name": "Bruno",
                     "last_name": "Ferreira", "password1": PW,
                     "password2": PW, "email": "Bruno@gmail.com"}
        userform = UserCreationForms(data_forg)
        userform.save()
        user = User.objects.get(username='Bruno')
        self.assertEqual(user.username, 'Bruno')

    def test_if_creating_user_as_existing_username(self):
        try:
            User.objects.create(username='Magaly', first_name='Ferreira',
                                last_name='Marcos', password=PW,
                                email='Mariana@gmail.com',
                                bio='textão',
                                is_staff=True, is_active=False)
        except:  # noqa: E722
            ERROR = 'UNIQUE constraint failed: Usuario_user.username'
        self.assertEqual(
            ERROR, 'UNIQUE constraint failed: Usuario_user.username')

    def test_if_creating_user_as_existing_email(self):
        try:
            User.objects.create(username='Mariana', first_name='Ferreira',
                                last_name='Marcos', password=PW,
                                email='Julia@gmail.com', bio='qualquer texto',
                                is_staff=True, is_active=False)
        except:  # noqa: E722
            ERROR = 'UNIQUE constraint failed: Usuario_user.email'
        self.assertEqual(ERROR, 'UNIQUE constraint failed: Usuario_user.email')
