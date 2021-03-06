# Generated by Django 2.0.4 on 2018-12-31 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aperturaNinos', '0008_auto_20181227_1845'),
        ('aperturaAdultos', '0012_auto_20181227_1748'),
        ('TerapiaOcupacional', '0005_auto_20181230_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaPaciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pacienteAdulto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aperturaAdultos.AperturaAdultos')),
                ('pacienteNiño', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aperturaNinos.HistoriaNiño')),
            ],
        ),
        migrations.RemoveField(
            model_name='terapiaocupacional',
            name='pacienteAdulto',
        ),
        migrations.RemoveField(
            model_name='terapiaocupacional',
            name='pacienteNiño',
        ),
        migrations.AddField(
            model_name='terapiaocupacional',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TerapiaOcupacional.ListaPaciente'),
        ),
    ]
