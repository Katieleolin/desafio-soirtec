# 🗳️ Desafio Soirtec - Enquetes da Katiele

Este é um projeto desenvolvido em **Django** para criação e gerenciamento de enquetes.  
O usuário pode votar em opções pré-definidas e visualizar os resultados em tempo real.

---

## 🚀 Tecnologias utilizadas
- [Python 3.x](https://www.python.org/)
- [Django 5.x](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/) (para estilização)
- HTML + CSS

---

## ⚙️ Como rodar o projeto localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/Katieleolin/desafio-soirtec.git
cd desafio-soirtec

### 2. Criar e ativar ambiente virtual
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

###3. Instalar dependências
pip install -r requirements.txt

###4. Rodar as migrações
python manage.py migrate

###5. Iniciar o servidor
python manage.py runserver
Acesse em: http://127.0.0.1:8000/

###📂 Estrutura do projeto
desafio-soirtec/
│── enquetes/        # App principal com as enquetes
│── mysite/          # Configurações do projeto Django
│── polls/           # Outro app de exemplo
│── manage.py        # Comando principal do Django
│── requirements.txt # Dependências do projeto

✨ Funcionalidades
Criar enquetes no painel administrativo

Votar em opções disponíveis

Visualizar resultados em tempo real

Interface simples e responsiva

👩‍💻 Autora
Projeto desenvolvido por Katiele como parte do desafio Soirtec. 📌 Meu GitHub

---







