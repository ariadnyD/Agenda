# Generated by Django 4.0.6 on 2022-12-16 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Materias',
            new_name='Materia',
        ),
        migrations.RenameModel(
            old_name='Tarefas',
            new_name='Tarefa',
        ),
    ]