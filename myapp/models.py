from django.db import models

class Status_das_tarefas(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return (self.nome)

class Materia(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return (self.nome)

class Tarefa(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=280)
    dataConclusao = models.DateField()
    status = models.ForeignKey(Status_das_tarefas, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        return (self.nome)

