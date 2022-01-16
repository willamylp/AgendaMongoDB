# Requisitos necessários:  
- Instalação do Selenium:  
```
   pip install selenium
```  
- Instalação do webDriverChrome:
O Webdriver para o navegador que você usará para testar seu projeto. Um WebDriver é uma API e protocolo para interagir e controlar o comportamento de um navegador específico. Como estamos usando o __Chrome__, faremos o download do driver do Chrome . Para obter uma lista de drivers para diferentes navegadores, visite a documentação do Selenium. Você também precisa adicionar o driver como um executável ao seu caminho, o que significa que o driver pode ser executado a partir do prompt de comando/terminal.
- link das ultimas versões disponivel [aqui](https://sites.google.com/chromium.org/driver/), 
- Para usuario [linux64](https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.41/)  
## Colocando nosso webdrive no path para utilizarmos ele: 
- Crie diretório ${HOME}/bin executando:
```  
   mkdir ${HOME}/bin
```  
- Extraia o arquivo .zip baixado e deixe ele sem pasta sem nada  dentro do diretorio do projeto.
- Mova para  o ${HOME}/bin:
```  
   mv chromedriver ${HOME}/bin
```  
- Torne o binary executável executando:
```
   chmod 755 ${HOME}/bin/chromedriver
```
- Abrir ${HOME}/.bash_profile em um editor de texto:
```  
   gedit ${HOME}/.bashrc
```
- Adicione linha export PATH="${PATH}:${HOME}/bin"ao arquivo e salve-o
- Reinicie seu Terminal
- Verify setup with chromedriver -v  
## executando o testes

