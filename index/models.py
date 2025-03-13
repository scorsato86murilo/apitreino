from django.db import models


class Index(models.Model):
    cidade_estado = models.CharField(max_length=100)
    rua_numero = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    img = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.cidade_estado


class Avisos(models.Model):
    mensagem = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data de criação da mensagem

    def __str__(self):
        return self.mensagem


class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data de criação do cadastro

    def __str__(self):
        return self.nome
