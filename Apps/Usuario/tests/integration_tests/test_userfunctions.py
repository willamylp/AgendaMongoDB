from Apps.Agenda.forms import AgendaForm
from Apps.Agenda.models import Contatos
from Apps.Usuario.models import User
from django.test import TestCase


# Create your views here.
class UsuarioTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='jorge',
                            first_name='Julia',
                            last_name='Ferreira',
                            password="ygfy4545#fhh",
                            email='jorge@gmail.com',
                            bio='qualquer textão',
                            is_staff=False,
                            is_active=False)
        Contatos.objects.create(contatosuser=1, nome="Bruno",
                                email="Bruno@gmail.com",
                                telefone=90903245)

    def tearDown(self):
        pass
        # self.one_user.delete()

    # def test_saval_contato_so_se_pertencer_a_um_usuario(self):
    #     form = AgendaForm(data_forg={"nome": "Mria",
    #                                          "email": "Mria@gmail.com",
    #                                          "telefone": 909032456})
    #     Contatos.form.save(commit=False)
    #     Contatos.contatosuser = User.objects.get(username="jorge")
    #     form.save()
    #     self.assertTrue(True)
