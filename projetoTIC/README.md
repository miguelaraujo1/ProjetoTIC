# Projeto 02 - Mini-projeto Web utilizando Docker + PostgreSQL

#### Membros da Equipe: 

#### Explicação do projeto: 
Este projeto é uma aplicação web desenvolvida com Flask, utilizando Docker para virtualização. O objetivo é criar um ambiente isolado que conecta a aplicação a um banco de dados PostgreSQL.

Arquivos do Projeto:

app.py: Contém o código principal da aplicação Flask, define rotas para requisições HTTP, processa consultas SQL e conecta ao PostgreSQL via psycopg2. As informações de conexão são resgatadas do docker-compose como variáveis de ambiente usando getenv, evitando colocá-las diretamente no código para melhorar a segurança. Além disso, foi criada uma classe chamada Config para melhorar a prática de programação relacionada à conexão com o banco de dados. Erros são tratados utilizando rollback para cancelar consultas indesejadas, e exceções são exibidas na página web.
index.html: Página principal que usa Jinja2 para renderizar consultas SQL e erros. Possui um formulário para entrada de comandos SQL.
styles.css: Define estilos visuais para a página web, melhorando a experiência do usuário.
Funcionamento dos Arquivos Docker:

docker-compose.yml: Define e gerencia serviços Docker, incluindo PostgreSQL, pgAdmin e a aplicação Flask.
projetotic-db: Serviço do banco de dados PostgreSQL.
projetotic-pgadmin: Interface de administração do PostgreSQL.
projetotic-web: Serviço da aplicação Flask, construído a partir de um Dockerfile. As informações de conexão ao banco de dados são especificadas como variáveis de ambiente.
Dockerfile: Contém os passos para construir a imagem da aplicação Flask, incluindo instalação de dependências e configuração do ambiente.
Execução do Projeto:

Instalar Docker e Docker Compose.
Navegar até o diretório do arquivo docker-compose.yml.
Executar sudo docker-compose up --build -d para iniciar os serviços.
Acessar a aplicação em http://localhost:5000.
Para parar e remover os contêineres, usar sudo docker-compose down.
