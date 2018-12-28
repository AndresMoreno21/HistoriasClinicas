# Generated by Django 2.0.4 on 2018-11-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenoresDeEdad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historia_del_contexto_educativo', models.TextField(max_length=500)),
                ('pautas_de_crianza', models.TextField(max_length=500)),
                ('caracteristicas_de_la_consulta', models.TextField(max_length=500)),
                ('conducta_durante_la_consulta', models.TextField(max_length=500)),
                ('escalas_aplicadas', models.TextField(max_length=500)),
                ('resultados_escalas_aplicadas', models.TextField(max_length=500)),
                ('impresion_diagnostica', models.TextField(max_length=500)),
                ('tratamiento', models.TextField(max_length=500)),
                ('evolucion', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Menor de edad',
            },
        ),
        migrations.CreateModel(
            name='Psicologia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('motivo_consulta', models.TextField(max_length=500)),
                ('percepcion_paciente', models.TextField(max_length=500)),
                ('sintomas', models.TextField(max_length=500)),
                ('antecendentes_del_motivo_de_consulta', models.TextField(max_length=500)),
                ('historia_familiar_relevante', models.TextField(max_length=500)),
                ('historia_personal', models.TextField(help_text='Desarrollo relevante.', max_length=500)),
                ('consumo_sustancias_psicoactivas', models.TextField(max_length=500)),
                ('tratamientos_psicologicos_o_psiquiatricos_previos', models.TextField(max_length=500)),
                ('antecedentes', models.TextField(help_text='Antecedentes de tipo psicologico, psiquiatricos y medicos familiares.', max_length=500)),
                ('conflictos_intrapsiquicos', models.TextField(max_length=500)),
                ('expectativas_del_paciente', models.TextField(max_length=500)),
                ('factores_de_riesgo', models.TextField(help_text='Factores de riesgo, protectores y predisponentes', max_length=500)),
                ('caracteristicas_cognitivas', models.TextField(max_length=500)),
                ('caracteristicas_sociales_y_relaciones_interpersonales', models.TextField(max_length=500)),
                ('caracteristicas_del_rango_afectivo_y_emocional', models.TextField(max_length=500)),
                ('caracteristicas_de_conducta', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Servicio de Psicologia',
            },
        ),
    ]
