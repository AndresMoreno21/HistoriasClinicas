# Generated by Django 2.0.4 on 2018-12-31 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aperturaNinos', '0008_auto_20181227_1845'),
        ('PsicologiaMenores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psicologiamenores',
            name='fecha',
        ),
        migrations.AddField(
            model_name='psicologiamenores',
            name='fecha_ingreso',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='psicologiamenores',
            name='pacienteNiño',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aperturaNinos.HistoriaNiño'),
            preserve_default=False,
        ),
    ]