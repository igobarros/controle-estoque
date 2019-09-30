# Controle de Estoque

## Como rodar o projeto ?

* Clone o repositório.
* Crie uma virtualenv com python 3.
* Ative a virtualenv.
* Instale as dependências.
* configure seu banco de dados
* Rode as migrações.

```
git clone https://github.com/IgoPereiraBarros/controle-estoque.git
cd controle-estoque
python3 -m venv .venv
pip install -r requirements.txt
python contrib/env_gen.py

No settings.py modifique o dicionário DATABASES, caso queira usar Mysql:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PW',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
## Rodando a aplicação com Docker

```
docker-compose up --build

```

* Rodando migrações dentro do container
```
docker-compose run web python manage.py migrate
```


# Teste dev

## Requisitos da solução
* Deve permitir o cadastro de novas mercadoria
* Deve ser registrado entrada e saída de mercadoria
* Preciso consultar o estoque de uma mercadoria e ver toda movimentação

## Observações: 
* A solução deve usar uma API em Django Rest Framework
Extra:
* Docker com um contêiner para cada aplicação
* Uso de NGINX 

## Avaliação:
Você deve publicar e enviar a URL da solução e acesso ao repositório GIT até dia 30/09/2019 - 08:00h.
* Analise da solução;
* Analise de código;
* Documentação e comentários de código; 
* Uso de ferramentas extra;
