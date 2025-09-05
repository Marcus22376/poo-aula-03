# aula-03 POO - 05/09/2025
abstração

# Rodar o container

    docker compose up -d


# Acessar o container no terminal

    docker exec -it aula-poo bash


# Executar os scripts Python
    python cadastro.py



# Atividades

### 1. No arquivo `cadastro.py` analise o código do CRUD (Create, Read, Update, Delete) e faça as seguintes modificações:
### a) adicione um ou mais campos/atributos ao cadastro de pessoas;
### b) modifique a lógica de Exclusão, para que seja solicitada uma confirmação ao tentar excluir uma pessoa;

### 2. Crie um arquivo chamado `atividade.py` para desenvolver uma aplicação que permita gerenciar clientes e seus empréstimos. A aplicação deve possibilitar o cadastro de clientes e o registro de múltiplos empréstimos para cada cliente. Ao final, o programa deve verificar e informar se cada cliente está apto a receber um novo empréstimo, considerando a regra de negócio do banco: um cliente não pode receber um novo empréstimo caso já tenha dois empréstimos pendentes de quitação ou ainda a dívida total de seus empréstimos ultrapasse o valor total de R$ 10.000,00. Utilize pelo menos duas classes (Cliente, Empréstimo) para estruturar a aplicação e organize o código de forma que reflita claramente os conceitos de abstração e relacionamento entre objetos.