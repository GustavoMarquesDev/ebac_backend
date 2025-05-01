# Django Admin Study Project

Este é um projeto Django criado para estudo e prática da página de administração do Django.

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Django 5.x
- SQLite (padrão, mas pode ser configurado para outro banco de dados)

## 📦 Instalação e Configuração

Siga os passos abaixo para rodar o projeto localmente.

### 1️⃣ Clone o repositório:

```sh
git clone https://github.com/GustavoMarquesDev/mysite
cd mysite
```

### 2️⃣ Crie um ambiente virtual e ative:

```sh
# No Windows
python -m venv venv
venv\Scripts\activate

# No Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instale as dependências:

```sh
pip install -r requirements.txt
```

### 4️⃣ Configure o banco de dados:

```sh
python manage.py migrate
```

### 5️⃣ Crie um superusuário para acessar o admin:

```sh
python manage.py createsuperuser
```

Digite um nome de usuário, e-mail e senha.

### 6️⃣ Inicie o servidor:

```sh
python manage.py runserver
```

Acesse o painel de administração em: http://127.0.0.1:8000/admin

## 📝 Funcionalidades

- Cadastro e gerenciamento de modelos via Django Admin
- Exploração de permissões e grupos de usuários

## 📜 Licença

Este projeto é apenas para fins de estudo. Fique à vontade para modificar e testar!


