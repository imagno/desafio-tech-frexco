# Desafio Tech (Automação) | Processo Seletivo Estágio Frexco

## Apresentação da proposta

Olá! Essa é a primeira etapa do nosso processo seletivo para vaga de Estágio em Desenvolvimento de Software (Automação). Dê o seu melhor :) 

Você já deve ter pesquisado sobre a empresa, mas aqui te conto um breve resumo sobre a Frexco: 

A Frexco é a principal ponte direta entre produtores e estabelecimentos do Brasil. Entregamos todas as semanas toneladas de alimentos recém colhidos para famílias e estabelecimentos e nosso objetivo é fomentar incessantemente que a cadeia de suprimentos seja mais justa. E tudo isso através da tecnologia! 

Então, para sabermos se você conseguirá nos ajudar no enorme desafio que temos no time de tecnologia hoje, preparamos um desafio para você! 

## Desafio Tech (Automação)

Construir pelo menos dois endpoints utilizando Django:

 - Cadastrar usuário, fornecendo o login, senha e data de nascimento;
 - Senha deixar como opcional, se não fornecido gerar uma senha aleatória;
 - Consultar usuários cadastrados;
 - Deve ser possível consultar em XLSX, CSV ou JSON;
 - Nos enviar em um repositório publico no GitHub ou plataforma similar.


# Início do Desafio Tech

## Utilização da api

Para ter acesso a api rode o comando abaixo no terminal e em seguida acesse o link:

*python3 manage.py runserver*

<http://127.0.0.1:8000/api/v1/usuarios>


Credenciais de acesso da API
 - Login: admin
 - Senha: admin

*Essas credenciais não são necessárias para cadastrar usuários*

_O campo *id* deve ser omitido do usuário quando for consumir a api no front-end_

O campo id será gerado automaticamente para melhor gestão dos cadastros de usuário.

*Foi criado o caminho /v1 como boa prática para o caso de uma futura atualização de versão não quebrar os sistemas de quem estiver utilizando a versão atual.*

### Endpoints

Foram gerados 7 endpoints diferentes automaticamente com a utilização do Django Rest Framework

URL                       | Método HTTP | Ação
--------------------------|-------------|------------------------------------
/api/v1                   | GET         | Raíz da API gerada automaticamente
/api/v1/usuarios          | GET         | Listagem de todos os usuários
/api/v1/usuarios          | POST        | Cadastro de novo usuário
/api/v1/usuarios/{lookup} | GET         | Recuperar usuário por ID
/api/v1/usuarios/{lookup} | PUT         | Atualização de usuário por ID
/api/v1/usuarios/{lookup} | PATCH       | Atualização parcial por ID
/api/v1/usuarios/{lookup} | DELETE      | Deleção de usuário por ID


_Aqui, {lookup} é o parâmetro utilizado pelo Django Rest Framework para identificar unicamente um elemento._

Vamos supor que exista um usuário de id: b5f81a8-9f16-416d-8371-83465b9b31ba

Para acessá-lo e realizar as alterações pretendidas basta substituir o {lookup} pela id do usuário.

## Considerações finais

Este foi o meu primeiro contato com Python, não consegui definir a senha gerada automaticamente como default para o campo de senha do usuário no arquivo models.py

Não sei dizer se o tipo da model tem que ser diferente do tipo CharField, se a função de gerar senha tem que ser declarada em outro arquivo e importada ou se tem algum outro motivo.

Este desafio acabou se mostrando bem interessante, aprender python passou a ser uma possibilidade futura.
