# Generated by Django 4.0.5 on 2022-12-27 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=280)),
                ('dataConclusao', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('AFA', 'A fazer'), ('AND', 'Em andamento'), ('FIN', 'Finalizada')], max_length=3)),
                ('arquivo', models.FileField(upload_to='files')),
                ('materia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.materia')),
            ],
        ),
    ]
