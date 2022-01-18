from django.test import TestCase
from django.urls import resolve, reverse
from django.http import Http404

class UsuarioTestViews(TestCase):

    #resolve() retorna um objeto da classe  ResolverMatch, que tem varios metodos de acesso,
    #se não tiver retorna uma except http404
    def test_urls_exists(self):
        resolver = resolve('/new/')
        self.assertEquals(resolver.url_name,'create_user')
    
    def test_view_loginUser_home_status_code_200(self):
        response = self.client.get(reverse('loginUser_home'))
        self.assertEquals(response.status_code, 200)
        
    def test_template_used_to_render_the_view(self):
        response = self.client.get(reverse('loginUser_home'))
        self.assertTemplateUsed(response,'index.html')


# Um uso possível de resolve()seria testar se uma visão geraria um Http404erro antes de redirecionar para ela:

# from urllib.parse import urlparse
# from django.urls import resolve
# from django.http import Http404, HttpResponseRedirect

# def myview(request):
#     next = request.META.get('HTTP_REFERER', None) or '/'
#     response = HttpResponseRedirect(next)

#     # modify the request and response as required, e.g. change locale
#     # and set corresponding locale cookie

#     view, args, kwargs = resolve(urlparse(next)[2])
#     kwargs['request'] = request
#     try:
#         view(*args, **kwargs)
#     except Http404:
#         return HttpResponseRedirect('/')
#     return response