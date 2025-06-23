# Formativa-PWBE2
Esta API foi desenvolvida com o objetivo de gerenciar um sistema escolar de forma prática e eficiente. Ela permite que gestores visualizem, excluam, atualizem e realizem atualizações parciais de usuários, salas, reservas de ambientes e disciplinas. Já os professores têm acesso apenas às informações relacionadas às suas próprias atividades, podendo visualizar suas salas, disciplinas e reservas de ambientes.

O sistema conta com validação de token para autenticação e controle de acesso. Apenas usuários com perfil de gestor possuem permissão para realizar operações de criação, edição e exclusão (CRUD), garantindo a segurança e integridade dos dados.

# Requisitos para Execução do Projeto:
  - O Python precisa estar devidamente instalado na máquina para possibilitar a execução do backend.
  - Para a gestão do banco de dados, é necessário ter o MySQL Workbench instalado, pois será utilizado para criar o banco de dados.

# Configuração do Banco de Dados
**1.** Abra o MySQL Workbench.

**2.** Crie um novo banco de dados com o seguinte comando:

   CREATE DATABASE cadastro;

No Projeto em settings.py é onde fica as configurações do seu banco de dados, em DATABASES, caso a sua configuração for diferente, o DATABASES terá que ser alterado.

# Preparando o Projeto
**1.** Clone o repositório do projeto:
git clone https://github.com/anadiasxavier/Formativa---PWBE2.git

**2.** Acesse a pasta do projeto pelo terminal:

cd Formativa---PWBE2

cd formativa

**3.** Abra o projeto no Visual Studio Code.

 code .
 
**4.** Acesse o terminal (atalho: Ctrl + J ou vá em Terminal > Novo Terminal).

**5.** Crie um ambiente virtual:

python -m venv venv

**6.** Ative o ambiente virtual:

.\venv\Scripts\activate

**7.** Instale as dependências do projeto:

pip install -r requirements.txt

**8.** Com o banco já criado, aplique as migrações:

python manage.py makemigrations

python manage.py migrate

**9.** Crie um superusuário para acessar o painel administrativo:

python manage.py createsuperuser

**10.**  Por fim, inicie o servidor:

python manage.py runserver


# Resolver problema no banco 

1° Apagar a pasta Pycache e Migrations 
2° Se tiver criado o banco, apagar o banco com ```drop database cadastro```
3° Criar o banco com ```create database cadastro```
4° Rodar no python ```python manage.py makemigrations app```
5° Rodar o migrate com ```python manage.py migrate```
6° Ser feliz 😊
