# Generated by Django 2.0.4 on 2019-01-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TerapiaOcupacional', '0008_auto_20190106_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_alimentacion',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_auditivo',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_cadera',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_cintura_escapular',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_deformaciones',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_funcion_muscular',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_funcion_postural',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_gustativo',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_higiene',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_movimientos_activos_y_pasivos',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_olfativo',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_pie',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_propioceptivo',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_rodilla',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_tactil',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_trofismo',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_vestibular',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_vestido',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='descripcion_visual',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='funcion_muscular',
            field=models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='funcion_postural',
            field=models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], max_length=2000),
        ),
        migrations.AlterField(
            model_name='terapiaocupacional',
            name='trofismo',
            field=models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], max_length=2000),
        ),
    ]
