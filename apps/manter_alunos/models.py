from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=30)
    sigla_estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=70)
    email = models.CharField(max_length=40)
    data_de_nascimento = models.CharField(max_length=60)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


