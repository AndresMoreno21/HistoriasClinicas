# Generated by Django 2.0.4 on 2018-12-31 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Psicologia', '0007_remove_psicologia_pacienteniño'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psicologia',
            name='fecha_ingreso',
        ),
        migrations.RemoveField(
            model_name='psicologia',
            name='motivo_consulta',
        ),
    ]
