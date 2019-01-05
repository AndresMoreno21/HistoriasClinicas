# Generated by Django 2.0.4 on 2018-12-31 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aperturaNinos', '0008_auto_20181227_1845'),
        ('aperturaAdultos', '0012_auto_20181227_1748'),
        ('TerapiaOcupacional', '0006_auto_20181231_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listapaciente',
            name='pacienteAdulto',
        ),
        migrations.RemoveField(
            model_name='listapaciente',
            name='pacienteNiño',
        ),
        migrations.RemoveField(
            model_name='terapiaocupacional',
            name='paciente',
        ),
        migrations.AddField(
            model_name='terapiaocupacional',
            name='pacienteAdulto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aperturaAdultos.AperturaAdultos'),
        ),
        migrations.AddField(
            model_name='terapiaocupacional',
            name='pacienteNiño',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aperturaNinos.HistoriaNiño'),
        ),
        migrations.DeleteModel(
            name='ListaPaciente',
        ),
    ]