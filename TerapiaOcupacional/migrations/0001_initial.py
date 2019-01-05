# Generated by Django 2.0.4 on 2018-11-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TerapiaOcupacional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movimientos_activos_y_pasivos', models.CharField(choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], max_length=20)),
                ('cintura_escapular', models.CharField(choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], help_text='Hombros', max_length=20)),
                ('cadera', models.CharField(choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], help_text='Pelvis', max_length=20)),
                ('rodilla', models.CharField(choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], help_text='Genu varus, genu valgus , movilidad, crujidos articulares.', max_length=20)),
                ('pie', models.CharField(choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], help_text='Equinus, talus, varus, valgus, planos, hallux valgus', max_length=20)),
                ('deformaciones', models.CharField(choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], help_text='Cifosis, lordosis, escoliosis, cifoescoliosis.', max_length=20)),
                ('tono_muscular', models.CharField(choices=[('Normal', 'Normal'), ('Hipertono', 'Hipertono'), ('Hipotono', 'Hipotono')], max_length=20)),
                ('actividad_refleja', models.CharField(choices=[('Normal', 'Normal'), ('Hipertono', 'Hipertono'), ('Hipotono', 'Hipotono')], max_length=20)),
                ('trofismo', models.CharField(choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], max_length=20)),
                ('funcion_muscular', models.CharField(choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], max_length=20)),
                ('funcion_postural', models.CharField(choices=[('Normal', 'Normal'), ('Alterado', 'Alterado')], max_length=20)),
                ('tactil', models.CharField(choices=[('Presentes', 'Presentes'), ('Ausentes', 'Ausentes')], max_length=10)),
                ('propioceptivo', models.CharField(choices=[('Presentes', 'Presentes'), ('Ausentes', 'Ausentes')], max_length=10)),
                ('vestibular', models.CharField(choices=[('Presentes', 'Presentes'), ('Ausentes', 'Ausentes')], max_length=10)),
                ('auditivo', models.CharField(choices=[('Presentes', 'Presentes'), ('Ausentes', 'Ausentes')], max_length=10)),
                ('gustativo', models.CharField(choices=[('Presentes', 'Presentes'), ('Ausentes', 'Ausentes')], max_length=10)),
                ('visual', models.CharField(choices=[('Presentes', 'Presentes'), ('Ausentes', 'Ausentes')], max_length=10)),
                ('olfativo', models.CharField(choices=[('Presentes', 'Presentes'), ('Ausentes', 'Ausentes')], max_length=10)),
                ('alimentacion', models.CharField(choices=[('Sin Apoyo', 'Sin apoyo'), ('Con Apoyo', 'Con apoyo')], max_length=10)),
                ('higiene', models.CharField(choices=[('Sin Apoyo', 'Sin apoyo'), ('Con Apoyo', 'Con apoyo')], max_length=10)),
                ('vestido', models.CharField(choices=[('Sin Apoyo', 'Sin apoyo'), ('Con Apoyo', 'Con apoyo')], max_length=10)),
                ('descanso', models.TextField(max_length=500)),
                ('educacion', models.TextField(max_length=500)),
                ('juego', models.TextField(max_length=500)),
                ('comps', models.BooleanField(default=False)),
                ('tepsi', models.BooleanField(default=False)),
                ('observaciones_clinicas', models.BooleanField(default=False)),
                ('sipt', models.BooleanField(default=False)),
                ('otras', models.TextField(blank=True, max_length=200)),
            ],
        ),
    ]