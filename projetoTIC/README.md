# Projeto 02 - Mini-projeto Web utilizando Docker + PostgreSQL

#### Membros da Equipe: 
Miguel Caetano - 06010623
Andrey Campos - 06009553
Nathan Salles - 06009233
Cristiano Cordeiro - 06010709
Gustavo Ramos - 06009333

Documentação Detalhada do Projeto: Aplicação Web com Flask e Docker
Descrição do Projeto

O projeto "ProjetoTIC" é uma aplicação web desenvolvida utilizando Flask e Docker. Ele tem como objetivo criar um ambiente isolado e escalável que conecta a aplicação a um banco de dados PostgreSQL. A aplicação permite realizar consultas SQL através de uma interface web, utilizando Jinja2 para renderização dinâmica e estilos CSS para melhorar a experiência do usuário.
Requisitos

Para executar este projeto em seu ambiente local, você precisará dos seguintes requisitos:

    Máquina virtual com sistema operacional Ubuntu instalado (pode ser configurada usando VirtualBox e a ISO do Ubuntu).
    Docker e Docker Compose instalados na máquina virtual.
    PostgreSQL e pgAdmin para gerenciamento do banco de dados.

Instalação da Máquina Virtual (VM) e Ubuntu
1. Instalação do VirtualBox

    Baixar e Instalar o VirtualBox:
        Acesse o site do VirtualBox através do seguinte link: VirtualBox
        Na página inicial, clique em "Downloads" no menu à esquerda.
        Selecione o pacote de instalação apropriado para seu sistema operacional hospedeiro (Windows, macOS, Linux, etc.) e siga as instruções de instalação fornecidas pelo instalador.

2. Preparação da Máquina Virtual

    Baixar a ISO do Ubuntu:
        Acesse o site oficial do Ubuntu para desktop através do link: Download do Ubuntu Desktop
        Escolha a versão desejada do Ubuntu e clique em "Download".
        Após o download, você terá um arquivo ISO do Ubuntu pronto para ser usado na instalação da máquina virtual.

    Configuração da Máquina Virtual no VirtualBox
        Abra o VirtualBox após a instalação.
        Clique em "Novo" para iniciar o assistente de criação de nova máquina virtual.
        Siga as etapas do assistente para configurar sua máquina virtual. Defina o nome, tipo e versão (Linux e Ubuntu, respectivamente).
        Aloque a quantidade de memória RAM desejada para a máquina virtual. Recomenda-se pelo menos 2GB para o Ubuntu.
        Escolha a opção "Criar um disco rígido virtual agora" e clique em "Criar".
        Selecione o tipo de arquivo de disco rígido virtual (VDI é o padrão recomendado) e clique em "Próximo".
        Escolha o tipo de alocação de espaço (dinamicamente alocado é geralmente recomendado) e defina o tamanho do disco.
        Clique em "Criar" para finalizar a criação da máquina virtual.

    Configurar o Boot com a ISO do Ubuntu
        Selecione a máquina virtual recém-criada na lista do VirtualBox e clique em "Configurações".
        Vá para a seção "Armazenamento", selecione o controlador de IDE e clique no ícone do disco ao lado do "Controlador: IDE".
        Escolha "Selecionar um arquivo de disco óptico virtual" e navegue até a ISO do Ubuntu que você baixou.
        Clique em "OK" para fechar as configurações.

Verificação e Instalação do Docker
1. Verificar se o Docker está Instalado

Para verificar se o Docker já está instalado, abra o terminal na sua máquina virtual Ubuntu e execute os seguintes comandos:

bash

docker --version
sudo systemctl status docker

Se o Docker estiver instalado, você verá a versão instalada e o status do serviço.
2. Instalação do Docker

Caso o Docker não esteja instalado, siga os passos abaixo para instalá-lo:

bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce
sudo usermod -aG docker $USER

Após a instalação, verifique se o Docker foi instalado corretamente:

bash

sudo systemctl status docker

Configuração do PostgreSQL e pgAdmin via Docker
1. Baixar e Configurar o PostgreSQL

    Baixar a Imagem do PostgreSQL:

    Execute o seguinte comando para baixar a imagem do PostgreSQL do DockerHub:

    bash

docker pull postgres

Criar uma Rede Docker

Crie uma rede Docker para permitir a comunicação entre os contêineres:

bash

docker network create pg-network

Configurar e Iniciar o Contêiner do PostgreSQL

Execute o seguinte comando para criar e iniciar o contêiner do PostgreSQL, substituindo sua_senha pela senha desejada:

bash

    docker run -d --name postgres-container -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 --network pg-network postgres

2. Baixar e Configurar o pgAdmin

    Baixar a Imagem do pgAdmin

    Execute o seguinte comando para baixar a imagem do pgAdmin do DockerHub:

    bash

docker pull dpage/pgadmin4

Configurar e Iniciar o Contêiner do pgAdmin

Execute o seguinte comando para criar e iniciar o contêiner do pgAdmin, substituindo seu_email e sua_senha pelos dados desejados:

bash

    docker run -d --name pgadmin-container -p 80:80 --network pg-network -e 'PGADMIN_DEFAULT_EMAIL=seu_email' -e 'PGADMIN_DEFAULT_PASSWORD=sua_senha' dpage/pgadmin4

    Acessar o pgAdmin
        Acesse o pgAdmin no navegador através do endereço: http://localhost:80
        Faça login com o e-mail e senha definidos anteriormente.
        No pgAdmin, vá para Servers -> Add New Server.
        Na guia Connection, em Host name/address, insira postgres-container.
        Use postgres como nome de usuário e a senha que você definiu para o PostgreSQL.

Execução da Aplicação Flask com Docker Compose
1. Clonar e Navegar até o Projeto

    Clonar o Repositório do Projeto

    Clone o repositório do projeto para sua máquina virtual:

    bash

    git clone https://github.com/miguelaraujo1/ProjetoTIC.git
    cd ProjetoTIC

2. Iniciar os Serviços com Docker Compose

Navegue até o diretório onde está localizado o arquivo docker-compose.yml e execute o seguinte comando para construir e iniciar os serviços definidos no Docker Compose em modo detached (-d):

bash

sudo docker-compose up --build -d

3. Acessar a Aplicação

Após a inicialização, acesse a aplicação web em seu navegador:

http://localhost:5000
4. Parar e Remover os Contêineres

Para parar e remover os contêineres Docker, execute:

bash

sudo docker-compose down
