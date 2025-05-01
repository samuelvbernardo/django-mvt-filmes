# Django MVT Filmes !

## 📖 Sobre o Projeto
Este é um projeto Django que utiliza o padrão **MVT (Model-View-Template)** para exibir uma lista de filmes. O objetivo é criar uma aplicação web simples e responsiva, onde os usuários podem visualizar informações sobre filmes, como título, ano de lançamento e imagens.

## 🚀 Funcionalidades
- Exibição de uma lista de filmes organizados em **cards**.
- Design responsivo utilizando **Bootstrap**.
- Modal para exibir informações detalhadas sobre os filmes.
- Administração dos filmes via django-admin, com imagens armazenadas na pasta media. 

## 🛠️ Tecnologias Utilizadas
- **Python**: Linguagem principal para o backend.
- **Django**: Framework web para desenvolvimento do backend.
- **HTML/CSS**: Estrutura e estilização da página.
- **Bootstrap**: Framework CSS para design responsivo.

## 📂 Estrutura do Projeto

```
django-mvt-filmes/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html              # Template base para herança
│   │   ├── filmes/
│   │       ├── listafilmes.html   # Página que exibe a lista de filmes
│   ├── __init__.py
│   ├── admin.py                   # Registro do modelo Filme no Django Admin
│   ├── apps.py                    # Configuração do app Django
│   ├── models.py                  # Definição do modelo Filme
│   ├── tests.py                   # Arquivo para testes automatizados
│   ├── urls.py                    # Rotas do app
│   ├── views.py                   # Lógica para renderizar a lista de filmes
├── filme/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                # Configurações do projeto Django
│   ├── urls.py                    # Rotas principais do projeto
│   ├── wsgi.py
├── media/
│   ├── filmes/                    # Imagens dos filmes
│       ├── filme1.jpg
│       ├── filme2.jpeg
│       ├── ...
├── static/
│   ├── filmes/
│       ├── assets/                
│       │   ├── fundo.jpeg         
|       |   ├── favicon.ico          
│       ├── css/
│       │   ├── bootstrap.min.css  # Estilos do Bootstrap
│       │   ├── style.css          # Estilos personalizados           
│       ├── js/
│           ├── bootstrap.bundle.min.js
├── manage.py                      # Comando de gerenciamento do Django
```

## ⚙️ Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior instalado.
- Virtualenv (opcional, mas recomendado).

### Passos

1. **Crie e ative um ambiente virtual**:
   No terminal, execute:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Instale as dependências**:
   ```cmd
   pip install -r requirements.txt
   ```

3. **Realize as migrações do banco de dados**:
   ```cmd
   python manage.py migrate
   ```

4. **Crie um superusuario (necessário para adicionar filmes)**:
   ```cmd
   python manage.py createsuperuser
   ```   

5. **Inicie o servidor de desenvolvimento**:
   ```cmd
   python manage.py runserver
   ```

6. **Acesse o projeto no navegador**:
   - URL: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🎨 Personalização
- **Adicionar Filmes**: Você pode adicionar filmes diretamente no banco de dados ou criar uma interface de administração para gerenciá-los.
- **Alterar o Estilo**: Modifique o arquivo `style.css` para personalizar o design ou modifique diretamente o html com Bootstrap.

## 📜 Licença
Este projeto está licenciado sob a MIT License — veja o arquivo [LICENSE](LICENSE) para detalhes.

## 💡 Autor
Desenvolvido por **Samuel Bernardo**. Entre em contato para dúvidas ou sugestões!
