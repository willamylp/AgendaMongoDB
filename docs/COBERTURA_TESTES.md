# Requisitos necessários 
Para calcular a cobertura dos nossos testes no django temos que fazer uma integração com coverage.py que possui uma documentação a ser vista em [coverage](https://coverage.readthedocs.io)

## Instalando o coverage: 
- Certifique-se de estar no mesmo diretorio que o manage.py
- Se não estiver listado no requirements.txt, Executar o comando no terminal:
```
   pip install coverage
``` 
## Executando a cobertura do projeto:
```
   coverage run --source='.' manage.py test Apps.Agenda Apps.Categoria Apps.Compartilhado Apps.Usuario
```
## Visualizar os resultados: 
```
   coverage report
```
Para uma melhor visualização:
```
   coverage html
```
Então uma pasta é gerada, a __htmlcov__ e então basta executar o *index.html* que se encontra dentro dela utilizando a extensão *live Server*.
