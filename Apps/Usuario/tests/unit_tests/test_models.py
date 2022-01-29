from Apps.Usuario.forms import UserCreationForms
from Apps.Usuario.models import User
# Create your tests here.
from django.test import TestCase


class UsuarioTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='Magaly', first_name='Julia',
                            last_name='Ferreira', password="ygfy4545#fhh",
                            email='Julia@gmail.com', bio='qualquer textão',
                            is_staff=False, is_active=False)

    def test_user_created_is_saved(self):
        data_forg = {"username": "Bruno", "first_name": "Bruno",
                     "last_name": "Ferreira", "password1": "ygfy4545#fhh",
                     "password2": "ygfy4545#fhh", "email": "Bruno@gmail.com"}
        userform = UserCreationForms(data_forg)
        userform.save()
        user = User.objects.get(username='Bruno')
        self.assertEqual(user.username, 'Bruno')

    def test_if_creating_user_as_existing_username(self):
        try:
            User.objects.create(username='Magaly', first_name='Ferreira',
                                last_name='Marcos', password="ygfy4545#fhh",
                                email='Mariana@gmail.com',
                                bio='qualquer textão',
                                is_staff=True, is_active=False)
        except:  # noqa: E722
            ERROR = 'UNIQUE constraint failed: Usuario_user.username'
        self.assertEqual(
            ERROR, 'UNIQUE constraint failed: Usuario_user.username')

    def test_if_creating_user_as_existing_email(self):
        try:
            User.objects.create(username='Mariana', first_name='Ferreira',
                                last_name='Marcos', password="ygfy4545#fhh",
                                email='Julia@gmail.com', bio='qualquer textão',
                                is_staff=True, is_active=False)
        except:  # noqa: E722
            ERROR = 'UNIQUE constraint failed: Usuario_user.email'
        self.assertEqual(ERROR, 'UNIQUE constraint failed: Usuario_user.email')
