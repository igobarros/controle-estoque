FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /projeto_controle_estoque
WORKDIR /projeto_controle_estoque
ADD requirements.txt /projeto_controle_estoque/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /projeto_controle_estoque/