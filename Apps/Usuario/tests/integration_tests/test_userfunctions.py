from Apps.Agenda.forms import AgendaForm
from Apps.Usuario.models import User
from django.test import TestCase


# Create your views here.
class UsersTestCase(TestCase):
    def setUp(self):
        self.us = User.objects.create(username='jofe', first_name='Julia',
                                      last_name='Ferreira',
                                      password="ygfy4545#fhh",
                                      email='jofe@gmail.com',
                                      bio='qualquer textão',
                                      is_staff=False,
                                      is_active=False)

    def tearDown(self):
        self.us.delete()

    def test_logic_view(self):
        data_forg = {"nome": "Mria",
                     "email": "Mria@gmail.com",
                     "telefone": 909032456}
        form = AgendaForm(data_forg)
        """ init """
        contato_falsificado = form.save(commit=False)  # type: ignore
        contato_falsificado.contatosuser = User.objects.get(username="jofe")
        form.save()
        """ the end """
        self.assertTrue(form.is_valid)
