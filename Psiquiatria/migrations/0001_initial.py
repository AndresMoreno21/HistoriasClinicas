# Generated by Django 2.0.4 on 2018-11-03 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miembro', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FamiliogramaPsiquiatria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.CharField(max_length=50)),
                ('parentezco', models.CharField(max_length=50)),
                ('escolaridad', models.CharField(max_length=50)),
                ('ocupacion', models.CharField(max_length=50)),
                ('miembro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Psiquiatria.Familiograma')),
            ],
        ),
        migrations.CreateModel(
            name='Psiquiatria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tratamiento', models.CharField(choices=[('PSICOLOGICO', 'Tratamiento Psicologico'), ('PSIQUIATRICO', 'Tratamiento Psiquiatrico')], max_length=20)),
                ('motivo_consulta', models.TextField(max_length=200)),
                ('diagnostico_actual', models.TextField(max_length=100)),
                ('historia_personal', models.TextField(max_length=200)),
                ('patologicos', models.CharField(max_length=30)),
                ('quirurgicos', models.CharField(max_length=30)),
                ('toxicos', models.CharField(max_length=30)),
                ('alegicos', models.CharField(max_length=30)),
                ('traumaticos', models.CharField(max_length=30)),
                ('ocupacionales', models.CharField(max_length=40)),
                ('antecedentes_familiares', models.CharField(max_length=50)),
                ('revision_por_sistemas', models.CharField(max_length=30)),
                ('examen_mental', models.CharField(max_length=30)),
                ('analisis', models.CharField(max_length=30)),
                ('diagnosticos', models.CharField(max_length=30)),
                ('plan_de_manejo', models.TextField(max_length=200)),
                ('recomendaciones', models.TextField(max_length=200)),
                ('miembro', models.ManyToManyField(through='Psiquiatria.FamiliogramaPsiquiatria', to='Psiquiatria.Familiograma')),
            ],
        ),
        migrations.AddField(
            model_name='familiogramapsiquiatria',
            name='psiquaitria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Psiquiatria.Psiquiatria'),
        ),
    ]
