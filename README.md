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
git clone https://github.com/seu-usuario/seu-repositorio.git
Substitua o link acima pelo link real do seu repositório no GitHub.

2. Acesse a pasta do projeto pelo terminal:

bash
Copiar
Editar
cd nome-da-pasta-do-projeto

**1.** Abra o projeto no Visual Studio Code.

**2.** Acesse o terminal (atalho: Ctrl + J ou vá em Terminal > Novo Terminal).

**3.** Crie um ambiente virtual:

python -m venv venv

**4.** Ative o ambiente virtual:

.\venv\Scripts\activate

**5.** Instale as dependências do projeto:

pip install -r requirements.txt

**6.** Com o banco já criado, aplique as migrações:

python manage.py makemigrations
python manage.py migrate

**7.** Crie um superusuário para acessar o painel administrativo:

python manage.py createsuperuser

**8.**  Por fim, inicie o servidor:

python manage.py runserver
