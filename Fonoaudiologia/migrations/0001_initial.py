# Generated by Django 2.0.4 on 2018-11-03 21:10

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fonoaudiologia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nariz_frente', models.CharField(choices=[('NORMAL', 'Normal'), ('DER', 'Desviada Derecha'), ('IZQ', 'Desviada Izquierda')], max_length=20)),
                ('nariz_perfil', models.CharField(choices=[('Normal', 'Normal'), ('Forma', 'Forma')], max_length=20)),
                ('nariz_vista_inferior', models.CharField(choices=[('NORMAL', 'Normal'), ('DER', 'Mayor Derecha'), ('IZQ', 'Mayor Izquierda')], max_length=20)),
                ('permeabilidad', models.CharField(choices=[('NARINA DER', 'Narina Dercha'), ('NARINA IZQ', 'Narina Izquierda')], max_length=20)),
                ('tamaño_labio_superior', models.CharField(choices=[('NORMAL', 'Normal'), ('CORTO', 'Corto'), ('FISURADO', 'Fisurado'), ('OPERADO', 'Operado')], max_length=100)),
                ('funcionalidad_labio_superior', models.CharField(choices=[('FUNCIONAL', 'Funcional'), ('NO FUNCIONAL', 'No Funcional')], max_length=20)),
                ('frenillo_labio_superior', models.CharField(choices=[('NORMAL', 'Normal'), ('CORTO', 'Corto'), ('TRANSFIXIANTE', 'Transfixiante')], max_length=20)),
                ('labio_inferior', models.CharField(choices=[('Normal', 'Normal'), ('Evertido', 'Evertido')], max_length=20)),
                ('evaluacion_intraoral', models.CharField(choices=[('Apertura Bucal Máxima', 'Apertura Bucal Máxima'), ('Con lengua en la papila', 'Con lengua en la papila')], max_length=30)),
                ('maxilar_superior', models.CharField(max_length=20)),
                ('maxilar_inferior', models.CharField(max_length=20)),
                ('intermaxilar_sagital', models.CharField(max_length=20)),
                ('intermaxilar_vertical', models.CharField(max_length=20)),
                ('intermaxilar_Transversal', models.CharField(max_length=20)),
                ('tamaño_lengua', models.CharField(choices=[('NORMAL', 'Normal'), ('AUMENTADO', 'Aumentado')], max_length=20)),
                ('frenillo_lengua', models.CharField(choices=[('NORMAL', 'Normal'), ('CORTO', 'Corto')], max_length=20)),
                ('forma_paladar_duro', models.CharField(choices=[('NORMAL', 'Normal'), ('ALTO', 'Alto'), ('FISURADO', 'Fisurado'), ('OPERADO', 'Operado')], max_length=30)),
                ('forma_paladar_blando', models.CharField(choices=[('NORMAL', 'Normal'), ('FISURADO', 'Fisurado'), ('OPERADO', 'Operado')], max_length=30)),
                ('uvula', models.CharField(choices=[('NORMAL', 'Normal'), ('BIFIDA', 'Bifida')], max_length=10)),
                ('amigdalas', models.CharField(choices=[('NORMALES', 'Normales'), ('AUMENTADAS_DER', 'Aumentadas Derecha'), ('AUMENTADAS_IZQ', 'Aumentadas Izquierda'), ('AUSENTES', 'Ausentes')], max_length=20)),
                ('posicion_lingual', models.CharField(choices=[('NORMAL', 'Normal'), ('DESCENDIDA', 'Descendida'), ('INTERPUESTA', 'Interpuesta')], max_length=20)),
                ('cierre_labial', models.CharField(choices=[('PRESENTE', 'Presente'), ('AUSENTE', 'Ausente'), ('CON ESFUERZO', 'Con Esfuerzo')], max_length=20)),
                ('tipo_respiracion', models.CharField(choices=[('COSTODIA', 'Costodriafragmatico'), ('COSTAL ALTO', 'Costal Alto'), ('MIXTO', 'Mixto')], max_length=20)),
                ('modo_respiracion', models.CharField(choices=[('NASAL', 'Nasal'), ('ORAL', 'Oral'), ('MIXTO', 'Mixto')], max_length=10)),
                ('malos_habitos', multiselectfield.db.fields.MultiSelectField(choices=[('Succión digital', 'Succión digital'), ('Onicofagia', 'Onicofagia'), ('Mamadera', 'Mamadera'), ('Chupete', 'Chupete'), ('Succión de Labio', 'Succión de Labio'), ('Succión de objetos', 'Succión de objetos')], max_length=79)),
                ('ejecucion_praxica', models.CharField(choices=[('NORMAL', 'Normal'), ('DISMINUIDA', 'Disminuida'), ('SIN MOVILIDAD', 'Sin Movilidad')], max_length=10)),
                ('praxias_labiales', multiselectfield.db.fields.MultiSelectField(choices=[('Protrusion de ambos labios', 'Protrusion de ambos labios'), ('Distension de ambos labios', 'Distension de ambos labios'), ('Desviacion de labios a comisura derecha', 'Desviacion de labios a comisura derecha'), ('Desviación de labios a comisura izquierda', 'Desviación de labios a comisura izquierda'), ('Retrusión labial sonora', 'Retrusión labial sonora'), ('Vibración labial', 'Vibración labial'), ('Inflar mejillas', 'Inflar mejillas')], max_length=192)),
                ('praxias_linguales', multiselectfield.db.fields.MultiSelectField(choices=[('Apex lingual recorre arcada dentaria superior', 'Apex lingual recorre arcada dentaria superior'), ('Apex lingual recorre arcada dentaria inferior', 'Apex lingual recorre arcada dentaria inferior'), ('Apex lingual recorre paladar duro', 'Apex lingual recorre paladar duro'), ('Adosamiento lingual', 'Adosamiento lingual'), ('Chasquido lingual', 'Chasquido lingual'), ('Vibración áfona en el alvéolo', 'Vibración áfona en el alvéolo'), ('Vibración lingual áfona entre los labios', 'Vibración lingual áfona entre los labios'), ('Elevación lingual extraoral', 'Elevación lingual extraoral'), ('Descenso lingual extraoral', 'Descenso lingual extraoral'), ('Lateralización de apex lingual a la derecha', 'Lateralización de apex lingual a la derecha'), ('Lateralización de apex lingual a la izquierda', 'Lateralización de apex lingual a la izquierda'), ('Apex lingual empuja mejilla derecha', 'Apex lingual empuja mejilla derecha'), ('Apex lingual empuja mejilla izquierda', 'Apex lingual empuja mejilla izquierda'), ('Apex lingual bajo labio superior', 'Apex lingual bajo labio superior'), ('Apex lingual bajo labio inferior', 'Apex lingual bajo labio inferior')], max_length=519)),
                ('bilabial', models.CharField(help_text='Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)', max_length=20)),
                ('labiodental', models.CharField(help_text='Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)', max_length=20)),
                ('post_dent_inf', models.CharField(help_text='Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)', max_length=20)),
                ('post_dent_sup', models.CharField(help_text='Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)', max_length=20)),
                ('alveolar', models.CharField(help_text='Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)', max_length=20)),
                ('palatal', models.CharField(help_text='Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)', max_length=20)),
                ('velar', models.CharField(help_text='Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)', max_length=20)),
                ('comp_lab_inf', models.CharField(help_text='Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)', max_length=20)),
                ('interdental', models.CharField(help_text='Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)', max_length=20)),
                ('retrocedido', models.CharField(help_text='Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)', max_length=20)),
                ('Omite', models.CharField(help_text='Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)', max_length=20)),
                ('observaciones', models.TextField(max_length=200)),
                ('tratamieto', models.TextField(max_length=200)),
            ],
        ),
    ]
