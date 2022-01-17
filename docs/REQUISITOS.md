## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:

Perfil                                 | Descrição   |
---------                              | ----------- |
Administrador | Este usuário pode realizar os cadastros, excluir cadastros base e pode realizar qualquer função dentro do sistema.
Usuário do sistema | Este usuário pode cadastrar, alterar, excluir seus proprios contatos  e pode compartilhar contatos com outros usuários.

## Lista de Requisitos Funcionais

Requisito                                 | Descrição   | Ator |
---------                                 | ----------- | ---------- |
RF001 - Realizar cadastro de Usuário | Um  novo usuário deve representar uma pessoa a qual seja utilizador do sistema. Um usuário tem: id, first_name, username, password , e-mail e bio. | Usuário/Administrador |
RF002 - Realizar alteração de senha Usuário |As informações de um Usuário poderão ser alteradas ou atualizadas. Um usuário tem: id, first_name, username, password , e-mail e bio . | Usuário/Administrador |
RF003 - Excluir um Usuário | As informações de um Usuário poderão ser excluídas. Um usuário tem: id, first_name, username, password , e-mail e bio . | Usuário/Administrador |
RF004 - Visualizar Usuários | As informações de um Usuário poderão ser visualizadas. Um usuário tem: id, first_name, username, password , e-mail e bio . | Administrador |  
RF005 - Permitir autenticação de usuário | Em posse das informações de username e password deverá ser autenticado no sistema. Um usuário tem: id, first_name, username, password , e-mail e bio . | Administrador/usuário |
RF006 - Criar um novo  Contato | Um  novo Contato deve ser criado no sistema. Um Contato tem: id, nome, e-mail e telefone | Usuário/Administrador |
RF007 - Alterar um  Contato  |  Um   Contato deve ser alterado no sistema. Um Contato tem:  id, nome, e-mail e telefone.  | Usuário/Administrador |
RF008 - Excluir um  Contato  |  Um   Contato deve ser alterado no sistema. Um Contato tem:  id, nome, e-mail e telefone.  | Usuário/Administrador |
RF009 - Exportar  registro de Contatos |  Realizar exportação em forma de arquivo,csv, excel ou pdf .  | Sistema  |
RF0010 - Compartilhar um  Contato  | Um  Contato deve ser compartilhado no sistema. Um Contato tem:   id, nome, e-mail e telefone. | Usuário/Administrador |
RF011 - Vizualizar Contatos | Os contatos pertencente ao usuário deverão ser visualizados pelo mesmo. | Sistema |
RF012 - Cadastrar uma nova categoria de contatos compartilhados |  categoria tem : id,tipo,descrição | Usuário/Administrador |
RF013 - Alterar uma nova categoria de contatos compartilhados |  categoria tem : id,tipo,descrição |Usuário/Administrador |
RF014 - Assegurar que uma categoria seja única | Categoria unica | Sistema |
RF015 - Visualizar Categorias | categoria tem : id,tipo,descrição |  Usuário/Administrador |
RF016 - Criar um compatilhamento de Contato |  Um  novo Contato deve ser compartilhado no sistema. Um Contato tem: id, nome, e-mail e telefone  |  Usuário/Administrador |
RF017 - Alterar dados de um compatilhamento |  Um  novo Contato compartilhado deve ser alterado no sistema. Um Contato tem: id, nome, e-mail e telefone  |  Usuário/Administrador |
RF018 - Assegurar que um compartilhamento seja unico | Ter um contato compartilhado somente 1 vez. Um Contato tem: id, nome, e-mail e telefone  | Sistema |
RF019 - Visualizar Contatos Compartilhados |  fazer a visualização dos contatos compartilhado no sistema. Um Contato tem: id, nome, e-mail e telefone  |  Usuário/Administrador 
RF020 - excluir um compartilhamento |  Realizar a exclusão de compartilhamento feito pelo mesmo Usuario que compartilhou. Um Contato tem: id, nome, e-mail e telefone  |  Usuário/Administrador





### Modelo Conceitual

Abaixo apresentamos o modelo conceitual usando o **YUML**.
![diagram](https://user-images.githubusercontent.com/54487740/141883250-9d854d69-7edc-4006-9638-d3afdf0e79c1.png)  

#### Descrição das Entidades

## Lista de Requisitos Não-Funcionais

Requisito                                 | Descrição   |
---------                                 | ----------- |
RNF001 - Deve ser acessível via navegador | Deve abrir perfeitamento no Firefox e principalmente no Chrome onde serão realizados testes com chrome webdrive. |
RNF002 - Consultas deve ser eficiente | O sistema deve executar as consultas em milessegundos |
RNF003 - Log e histórico de acesso e funções | Deve manter um log de todos os acessos e das funções executadas pelo usuário |
