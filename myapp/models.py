from django.db import models
from django.contrib.auth.models import User

class Materia(models.Model):
    codigo = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)

    def __str__(self):
        return (self.nome)

class Tarefa(models.Model):
    status_choice = (
        ("AFA","A fazer"),
        ("AND","Em andamento"),
        ("FIN","Finalizada"),
    )
    codigo = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=280)
    dataConclusao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=3, choices=status_choice)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True, blank=True)
    arquivo = models.FileField(upload_to="files", null=True, blank=True)

    def __str__(self):
        return (self.nome)

