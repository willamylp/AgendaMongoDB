# Requisitos necessários: 
Para o projeto não é necessário nenhuma instalação quanto a execução dos testes de unidade, pois ao criar um projeto django ele já nos dispõem do framework de teste mais utilizado no python, o *unittest*. Ele foi originalmente inspirado no JUnit e tem um estilo semelhante contendo as principais estruturas de teste de unidades existentes em outras linguagens. Ele suporta a automação de testes, compartilhamento de configuração e código de desligamento para testes, agregação de testes em coleções e independência dos testes do framework de relatórios. Para saber mais sobre ele consulte: [unittest](https://docs.python.org/pt-br/3/library/unittest.html) 


## Executando os testes de uma app: 
- Certifique-se de estar no mesmo diretorio que o manage.py
- Executar o comando no terminal para cada uma das app que queira testar ex:
```
   python3 manage.py test Apps.Inscricao
```