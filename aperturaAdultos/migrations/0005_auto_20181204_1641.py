# Generated by Django 2.0.4 on 2018-12-04 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TerapiaOcupacional', '0002_auto_20181105_2006'),
        ('Psicologia', '0003_delete_menoresdeedad'),
        ('aperturaAdultos', '0004_aperturaadultos_terapiaocupacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtensionServicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psicologia', models.ManyToManyField(to='Psicologia.Psicologia')),
                ('terapiaOcupacion', models.ManyToManyField(to='TerapiaOcupacional.TerapiaOcupacional')),
            ],
        ),
        migrations.RemoveField(
            model_name='aperturaadultos',
            name='terapiaOcupacion',
        ),
    ]
