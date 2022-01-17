# Agenda - Site
Agenda de Contatos usando Python Django  
## Descrição:  
A Agenda é um projeto que consiste na coleta e repositório de dados dos seus contatos através de um backup online. Dessa forma, você consegue acessar tais informações em qualquer momento e em qualquer dispositivo. A página funciona através de um sistema de login que dará acesso a uma página central da qual conseguirá gerir os dados de seus contatos. Ademais, consegue gerar um relatório (pdf, excel, etc) com todos os dados cadastrados.  
## Documentação:
[Requisitos + Modelo](https://github.com/willamylp/AgendaMongoDB/blob/develop/docs/REQUISITOS.md)  
[Documento de Visão](https://github.com/willamylp/AgendaMongoDB/blob/develop/docs/doc-visao.md)  
[User Stories](https://github.com/willamylp/AgendaMongoDB/blob/develop/docs/doc-userstories.md)


## Equipe:
[Clodoaldo Brito](https://github.com/Brito-Response)  
[Gesson Brener](https://github.com/gersonferreirarn)  
[Willamy Domingos](https://github.com/willamylp)  
[Gustave Persijn](https://github.com/gpersijn) 

## Tecnologias, Frameworks e bibliotecas de Testes:  
- Python(Django).  
- unittest - este framework de teste é adequado para testes unitários e de integração.  
- LiveServerTestCase - ferramenta para usar diferentes frameworks de teste.  
- Selenium - framework para simular um usuário interagindo com um navegador.
   

## Ferramentas necessárias para execução do projeto no Windows:
* Python 3.7 + pip  
* Criar uma Virtual ENV 
    ```
    pip install virtualenv
    virtualenv virtualENV
    ```
* Ativar Venv
    ```
    . virtualENV/Scripts/Activate
    ```  

## Passo a passo para rodar o projeto : 
- Baixar todas as Dependencias, é preciso estar dentro da pasta do projeto no mesmo diretorio que o requirements-dev.txt:
    ```
    pip install -r requirements.txt
    ```
- Renomer o arquivo __.env.example__ para somente __.env__.  
- **OBS: Fazer as migraçỗes e aplicação das migrations no bd para cada app localizada dentro da pasta App(suas) especificada, Usuario, Agenda e etc...**
- Quando colocado dentro de um pacote como "App" temos que forçar o django a encontrar a app especificadas pois por padão ele procura apenas no mesmo diretório que esta o manage.py.
- **Executando e aplicando todas de uma só vez:**   
    ```
    python manage.py makemigrations Usuario
    python manage.py migrate Usuario
    python manage.py makemigrations Categoria
    python manage.py migrate Categoria
    python manage.py makemigrations Agenda
    python manage.py migrate Agenda
    python manage.py makemigrations Compartilhado
    python manage.py migrate Compartilhado
    python manage.py migrate
    cls

    ```  
- Criar Usuario admin:
    ```
    python manage.py createsuperuser
    ```  
    
- Rodar:
    ```
    python manage.py runserver
    ```
E visualizar no navegador no http://127.0.0.1:8000/  
## Ferramentas necessárias para execução do projeto no Ubuntu:
* Python 3.7 + Python3-venv

* Criar uma Virtual ENV 
    ```
    sudo apt-get install python3-venv && \
    python3 -m venv virtualENV
    ```
* Ativar Venv
    ```
    . virtualENV/bin/activate ou source virtualENV/bin/activate
    ```  

## Passo a passo para rodar o projeto : 
- Baixar todas as Dependencias, é preciso estar dentro da pasta do projeto no mesmo diretorio que o requirements-dev.txt:
    ```
    pip3 install -r requirements.txt
    ```
- Renomer o arquivo __.env.example__ para somente __.env__.  
- **OBS: Fazer as migraçỗes e aplicação das migrations no bd para cada app localizada dentro da pasta App(suas) especificada, Usuario, Agenda e etc...**
- Quando colocado dentro de um pacote como "App" temos que forçar o django a encontrar a app especificadas pois por padão ele procura apenas no mesmo diretório que esta o manage.py.
- **Executando e aplicando todas de uma só vez:**   
    ```
    python3 manage.py makemigrations Usuario && \
    python3 manage.py migrate Usuario && \
    python3 manage.py makemigrations Categoria && \
    python3 manage.py migrate Categoria && \
    python3 manage.py makemigrations Agenda && \
    python3 manage.py migrate Agenda && \
    python3 manage.py makemigrations Compartilhado && \
    python3 manage.py migrate Compartilhado && \
    python3 manage.py migrate
    ```  
- Criar Usuario admin:
    ```
    python3 manage.py createsuperuser
    ```  
    
- Rodar:
    ```
    python3 manage.py runserver
    ```
E visualizar no navegador no http://127.0.0.1:8000/


## Em caso de erro verifique  
- verifique se seguiu os passos de execução corretamente.  
- Faça a exclusão dos arquivos de cache gerados, das migrations e do banco de dados db.sqlite3 e execute as instruções acima novamente.  
## Informações e Ferramentas necessárias para execução dos Testes  projeto:  
[Teste de Unidade](https://github.com/willamylp/AgendaMongoDB/tree/develop/docs/TESTE_UNIDADE.md)  
[Teste de Integração](https://github.com/willamylp/AgendaMongoDB/tree/develop/docs/TESTE_INTEGRACAO.md)  
[Cobertura Dos Testes](https://github.com/willamylp/AgendaMongoDB/tree/develop/docs/COBERTURA_TESTES.md)  
[Testes Funcionais Automatizados](https://github.com/willamylp/AgendaMongoDB/tree/develop/docs/TESTE_FUNC_AUTOMATIZADOS.md)