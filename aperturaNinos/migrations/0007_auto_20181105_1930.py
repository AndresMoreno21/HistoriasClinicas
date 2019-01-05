# Generated by Django 2.0.4 on 2018-11-06 00:30

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aperturaNinos', '0006_historianiño_medicamentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='historianiño',
            name='descripcion_problema_socio',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historianiño',
            name='historia_socio_familiar',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Conflictos de pareja', 'Conflictos de pareja'), ('Conflictos entre padres e hijos', 'Conflictos entre padres e hijos'), ('Conflictos entre hermanos', 'Conflictos entre hermanos'), ('Pérdidas o duelos', 'Pérdidas o duelos'), ('Consumo de alcohol o spa', 'Consumo de alcohol o spa'), ('Dificultades en manejo de autoridad', 'Dificultades en manejo de autoridad')], max_length=157),
        ),
    ]