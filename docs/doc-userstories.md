# Documento Lista de User Stories

Documento construído a partido do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no
link: https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](doc-visao.md). Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 22/06/2020 | 0.0.1   | Template e descrição do documento  | Taciano de Morais Silva |
| 23/06/2020 | 0.0.2   | Detalhamento do User Story US01    | Taciano de Morais Silva |
| ...        | ...     | ...                                | ...     |
| 12/07/2020 | 1.0.0   | Documento completo com o detalhamento de todos os User Stories | Taciano     |



### User Story US01 - Manter Usuário

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um cadastro de usuário que tem acesso ao sistema via login e senha. Um usuário tem os atributos name, id, email, username, data de nascimento, tipo de usuário, status, password, avatarURL. O email será o login e ele pode registrar-se diretamente no sistema, o avatarURL é um link para uma foto de seu perfil. Além disso o usuário poderá alterar alguns dados, como o e-mail ou a senha. O usuário administrador do sistema pode realizar as operações de adicionar, alterar, remover e listar os usuários comuns do sistema. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Cadastrar Usuário |
| RF02          | Alterar Usuário  |
| RF03          | Excluir Usuário        |
| RF04          | Vizualizar detalhes do Usuário |
| RF05          | Permitir autenticação de  Usuário |

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 7 PF                                |

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | Ao acessar a tela de login do usuário, o mesmo deve conseguir através de link ser redirecionado para uma página onde consiga preencher suas informações e cadastre-se no sistema, garantindo acesso. |
| **TA01.01.N** | Em caso do não preenchimento das informações corretas ou obrigatórias, o sistema não deve permitir acesso ao usuário em questão. |
| **TA01.02** | Ao solicitar a alteração de seus dados no sistema, o usuário em questão deve visualizar suas informaçoẽs antigas e conseguir alterar para as mais atuais. |
| **TA01.02.N** | No caso de informações de informações inesperadas pelo sistema, o usario deverá ser notificado ou receber feedback de alguma forma enquanto não estiver conseguindo alterar um dado.|
| **TA01.03** | Quando solicitado pelo admin qualquer usuário dentro do sistema tera a exclusão de sus informações consolidada, com confirmação necessaria. |
| **TA01.03.N** | Caso haja a não confirmação o usuário  volta a ter e visualizar suas informações normalmente. |
| **TA01.04** | Se solicitado para visualizar as suas informações o Usuário/Admin pode ver em detalhes. |
| **TA01.05** | Se solicitado a autenticação do usuário o Usuário/Admin deverá visualizar, acrescentar/atualizar suas informações acrescentadas no sistema. |
| **TA01.05.N** | Caso usuário não consiga de autenticar o mesmo não tera acesso as informações, nem sera autorizado  poder ter acesso a outras paginas que seja a de login. |

