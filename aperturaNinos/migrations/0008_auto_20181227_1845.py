# Generated by Django 2.0.4 on 2018-12-27 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperturaNinos', '0007_auto_20181105_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historianiño',
            name='identificacion',
            field=models.CharField(max_length=50),
        ),
    ]