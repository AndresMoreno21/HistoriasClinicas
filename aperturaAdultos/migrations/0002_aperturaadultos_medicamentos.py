# Generated by Django 2.0.4 on 2018-11-03 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperturaAdultos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aperturaadultos',
            name='medicamentos',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
