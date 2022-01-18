from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from Apps.Usuario.models import User

class UsuarioTestCase(TestCase):
    def setUp(self):
        User.objects.create( username ='Magaly', first_name = 'Julia',
        last_name = 'Ferreira',password="ygfy4545#fhh", email = 'Julia@gmail.com',
        bio = 'qualquer textão', is_staff=False, is_active = False)


    def test_user_created_is_saved(self):
        user = User.objects.get(username ='Magaly')
        self.assertEquals(user.username,'Magaly')

    
    def test_if_creating_user_as_existing_username(self):
        try:
            User.objects.create( username ='Magaly', first_name = 'Ferreira',
            last_name = 'Marcos',password="ygfy4545#fhh", email = 'Mariana@gmail.com', bio = 'qualquer textão', is_staff=True, is_active = False)
        except:
            ERROR = 'UNIQUE constraint failed: Usuario_user.username'
        self.assertEqual(ERROR,'UNIQUE constraint failed: Usuario_user.username')

    def test_if_creating_user_as_existing_email(self):
        try:
            User.objects.create( username ='Mariana', first_name = 'Ferreira',
            last_name = 'Marcos',password="ygfy4545#fhh", email = 'Julia@gmail.com', bio = 'qualquer textão', is_staff=True, is_active = False)
        except:
            ERROR = 'UNIQUE constraint failed: Usuario_user.email' 
        self.assertEqual(ERROR,'UNIQUE constraint failed: Usuario_user.email')