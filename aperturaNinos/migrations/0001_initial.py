# Generated by Django 2.0.4 on 2018-11-03 21:10

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaNiño',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_identificacion', models.CharField(choices=[('Registro Civil ', 'Registro Civil'), ('Tarjeta Identidad', 'Tarjeta Identidad')], max_length=50)),
                ('eps', models.CharField(choices=[('Medimas', 'Medimas'), ('Emssanar', 'Emssanar'), ('Nueva EPS', 'Nueva EPS'), ('Sanitas', 'Sanitas'), ('Comfamiliar de nariño', 'Comfamiliar de nariño'), ('Policia Nacional', 'Policia Nacional'), ('Ejercito Nacional', 'Ejercito Nacional'), ('Particular', 'Particular')], max_length=100)),
                ('fecha_ingreso', models.DateField()),
                ('institucion_educativa', models.CharField(max_length=50)),
                ('nivel_educativo', models.CharField(choices=[('PARVULOS', 'Parvulos'), ('Pre Jardin', 'Pre Jardin'), ('Jardin', 'Jardin'), ('Transicion', 'Transicion'), ('Primero', 'Primero'), ('Segundo', 'Segundo'), ('Tercero', 'Tercero'), ('Cuarto', 'Cuarto'), ('Quinto', 'Quinto'), ('Sexto', 'Sexto'), ('Septimo', 'Septimo'), ('Octavo', 'Octavo'), ('Noveno', 'Noveno'), ('Decimo', 'Decimo'), ('Once', 'Once'), ('Universitario', 'Universitario')], max_length=20)),
                ('primer_nombre_madre', models.CharField(help_text='Primer Nombre', max_length=50)),
                ('segundo_nombre_madre', models.CharField(max_length=50)),
                ('primer_apellido_madre', models.CharField(max_length=50)),
                ('segundo_apellido_madre', models.CharField(max_length=50)),
                ('fecha_nacimiento_madre', models.CharField(max_length=100)),
                ('ocupacion_madre', models.CharField(max_length=50)),
                ('primer_nombre_padre', models.CharField(max_length=50)),
                ('segundo_nombre_padre', models.CharField(max_length=50)),
                ('primer_apellido_padre', models.CharField(max_length=50)),
                ('segundo_apellido_padre', models.CharField(max_length=50)),
                ('fecha_nacimiento_padre', models.CharField(max_length=100)),
                ('ocupacion_padre', models.CharField(max_length=50)),
                ('diagnostico_principal', models.TextField(max_length=100)),
                ('diagnostico_secundario', models.TextField(max_length=100)),
                ('antecedentes_embarazo', multiselectfield.db.fields.MultiSelectField(choices=[('CONTROL MEDICO', 'Control Medico'), ('ANEMIA', 'Anemia'), ('Presion Arterial alta', 'Presion Arterial alta'), ('TOXEMIA', 'Toxemia'), ('Enfermedades del riñon', 'Enfermedades del riñon'), ('Problemas del Corazón', 'Problemas Del Corazón'), ('Amenaza de Aborto', 'Amenaza de Aborto'), ('Hospitalizaciones o Cirugias', 'Hospitalizaciones o Cirugias'), ('Consumo de Cigarrillo, Alcohol, otras sustancias', 'Consumo de Cigarrillo, Alcohol, Otras sustancias'), ('Problemas emocionales', 'Problemas Emocionales'), ('Sangrando o Hemorragias', 'Sangrando o Hemorragias'), ('BROTES', 'Brotes'), ('Enfermedades Cronicas', 'Enfermedades Cronicas'), ('RH u otra incompatibilidad de sangre', 'RH u otra incompatibilidad de sangre'), ('Otras Lesiones', 'Otras Lesiones'), ('Infecciones', 'Infecciones')], max_length=331)),
                ('causa_hospitalizacion', models.TextField(max_length=100)),
                ('parto', models.CharField(choices=[('A termino', 'A termino'), ('Prematuro', 'Prematuro'), ('Cesarea', 'Cesarea')], max_length=100)),
                ('edad_en_la_que_sostuvo_la_cabeza', models.CharField(help_text='Meses', max_length=10)),
                ('edad_en_la_que_se_sento_solo', models.CharField(help_text='Meses', max_length=10)),
                ('edad_en_la_que_gateo', models.CharField(help_text='Meses', max_length=10)),
                ('edad_en_la_que_camino_sin_apoyo', models.CharField(help_text='Meses', max_length=10)),
                ('edad_en_la_que_dijo_las_primeras_palabras', models.CharField(help_text='Meses', max_length=10)),
                ('edad_en_la_que_dijo_frases_simples', models.CharField(help_text='Meses', max_length=10)),
                ('edad_en_la_que_se_expreso_sin_errores_fonologicos', models.CharField(help_text='Años', max_length=10)),
                ('edad_en_la_que_inicio_lecto_escritura', models.CharField(help_text='Años', max_length=10)),
                ('conducta', multiselectfield.db.fields.MultiSelectField(choices=[('Dificultad en control de esfínteres', 'Dificultad en control de esfínteres'), ('Se lleva bien con niños', 'Se lleva bien con niños'), ('Es tímido', 'Es tímido'), ('Inmaduro', 'Inmaduro'), ('Impulsivo', 'Impulsivo'), ('Hace rabietas', 'Hace rabietas'), ('Comportamiento extraño', 'Comportamiento extraño'), ('Problemas del sueño', 'Problemas del sueño'), ('Tiene ausencias', 'Tiene ausencias'), ('Tics o movimientos bruscos', 'Tics o movimientos bruscos'), ('Independencia acorde a su edad', 'Independencia acorde a su edad'), ('Conducta agresiva', 'Conducta agresiva'), ('Rebeldia', 'Rebeldia'), ('Mas activo que otros niños', 'Mas activo que otros niños'), ('Conductas de riesgo', 'Conductas de riesgo'), ('Conflictos con la ley', 'Conflictos con la ley'), ('Consumo de sustancias', 'Consumo de sustancias'), ('Dificultades en relaciones', 'Dificultades en relaciones')], max_length=364)),
                ('historia_medica', multiselectfield.db.fields.MultiSelectField(choices=[('Lesiones en la cabeza', 'Lesiones en la cabeza'), ('Infecciones de oido', 'Infecciones de oido'), ('Dificultades visuales', 'Dificultades visuales'), ('Hospitalizaciones', 'Hospitalizaciones'), ('Convulsiones', 'Convulsiones'), ('Problemas emocionales', 'Problemas emocionales'), ('Problemas de adaptacion', 'Problemas de adaptacion'), ('Problemas de conducta', 'Problemas de conducta'), ('Padeció meningitis o encefalitis', 'Padeció meningitis o encefalitis'), ('Asma', 'Asma'), ('Diabetes', 'Diabetes'), ('Retraso de crecimiento', 'Retraso de crecimiento'), ('Alergias', 'Alergias'), ('Ha recibido tratamiento psicologico psiquiatrico', 'Ha recibido tratamiento psicologico psiquiatrico'), ('Se queja del dolor de cabeza', 'Se queja del dolor de cabeza'), ('Se queja del dolor de estomago', 'Se queja del dolor de estomago'), ('Cirugias', 'Cirugias'), ('Problemas en la alimentacion', 'Problemas en la alimentacion'), ('Problemas de tiroides', 'Problemas de tiroides'), ('Historia cardiovascular', 'Historia cardiovascular')], max_length=434)),
                ('historia_escolar', multiselectfield.db.fields.MultiSelectField(choices=[('Dificultad en adaptacion', 'Dificultad en adaptacion'), ('Dificultad en Socializacion', 'Dificultad en Socializacion'), ('Necesidad de apoyo adicional', 'Necesidad de apoyo adicional'), ('Deserción escolar', 'Deserción escolar'), ('Dificultades en aprendizaje de lectura', 'Dificultades en aprendizaje de lectura'), ('Dificultades en aprendizaje de escritura', 'Dificultades en aprendizaje de escritura'), ('Dificultades en aprendizaje de aritmética', 'Dificultades en aprendizaje de aritmética'), ('Fracaso escolar', 'Fracaso escolar')], max_length=237)),
                ('historia_socio_familiar', multiselectfield.db.fields.MultiSelectField(choices=[('Conflictos de pareja', 'Conflictos de pareja'), ('Conflictos entre padres e hijos', 'Conflictos entre padres e hijos'), ('Conflictos entre hermanos', 'Conflictos entre hermanos'), ('Pérdidas o duelos', 'Consumo de Alcohol o spa')], max_length=96)),
            ],
        ),
    ]
