# Generated by Django 2.0.4 on 2018-11-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperturaAdultos', '0002_aperturaadultos_medicamentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturaadultos',
            name='ingreso',
            field=models.CharField(max_length=100),
        ),
    ]
