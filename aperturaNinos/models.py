# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.



ANTECEDENTES_EMBARAZO =(
		('CONTROL MEDICO','Control Medico'),
		('ANEMIA','Anemia'),
		('Presion Arterial alta','Presion Arterial alta'),
		('TOXEMIA','Toxemia'),
		('Enfermedades del riñon','Enfermedades del riñon'),
		('Problemas del Corazón','Problemas Del Corazón'),
		('Amenaza de Aborto','Amenaza de Aborto'),
		('Hospitalizaciones o Cirugias','Hospitalizaciones o Cirugias'),
		('Consumo de Cigarrillo, Alcohol, otras sustancias','Consumo de Cigarrillo, Alcohol, Otras sustancias'),
		('Problemas emocionales','Problemas Emocionales'),
		('Sangrando o Hemorragias','Sangrando o Hemorragias'),
		('BROTES','Brotes'),
		('Enfermedades Cronicas','Enfermedades Cronicas'),
		('RH u otra incompatibilidad de sangre','RH u otra incompatibilidad de sangre'),
		('Otras Lesiones','Otras Lesiones'),
		('Infecciones','Infecciones'),
	)

TIEMPO_PARTO = (
		('A TERMINO', 'A Termino'),
		('PREMATURO', 'Prematuro'),
		)

TIPO_PARTO = (
		('NATURAL', 'Natural'),
		('CESAREA', 'Cesarea'),
		)


TIPO_IDENTIFICACION = (
	('Registro Civil ', 'Registro Civil'),
	('Tarjeta Identidad', 'Tarjeta Identidad'),
	)

NIVEL_EDUCATIVO=(
		('PARVULOS','Parvulos'),
		('Pre Jardin','Pre Jardin'),
		('Jardin','Jardin'),
		('Transicion','Transicion'),
		('Primero','Primero'),
		('Segundo','Segundo'),
		('Tercero','Tercero'),
		('Cuarto','Cuarto'),
		('Quinto','Quinto'),
		('Sexto','Sexto'),
		('Septimo','Septimo'),
		('Octavo','Octavo'),
		('Noveno','Noveno'),
		('Decimo','Decimo'),
		('Once','Once'),
		('Universitario','Universitario'),
	)

EPS_CHOICES = (

	('Medimas', 'Medimas'),
	('Emssanar', 'Emssanar'),
	('Nueva EPS', 'Nueva EPS'),
	('Sanitas', 'Sanitas'),
	('Comfamiliar de nariño', 'Comfamiliar de nariño'),
	('Policia Nacional', 'Policia Nacional'),
	('Ejercito Nacional', 'Ejercito Nacional'),
	('Particular', 'Particular'),
    )

PARTO_CHOICES = (

	('A termino', 'A termino'),
	('Prematuro', 'Prematuro'),
	('Cesarea', 'Cesarea'),
	('Inducido', 'Inducido'),
	('Prolongado', 'Prolongado'),
	('Sufrimiento fetal', 'sufrimiento fetal'),
	('Presentacion podalica', 'presentacion podalica'),
	('Se usó forceps', 'se usó forceps'),
	('Anoxia', 'Anoxia'),
	('Complicaciones', 'Complicaciones'),
	('Problemas respiratorios', 'Problemas respiratorios'),
	('Cordon umbilical al cuello', 'Cordon umbilical al cuello'),
	('Requirio fototerapia', 'Requirio fototerapia'),
	('Llanto debil', 'Llanto debil'),
	('Requirio transfuciones', 'Requirio transfuciones'),
	('Requirio respirador', 'Requirio respirador'),
	('Problemas con la alimentacion', 'Problemas con la alimentacion'),
	('Bebe activo', 'Bebe activo'), 
)

CONDUCTA_CHOICES = (

	('Dificultad en control de esfínteres', 'Dificultad en control de esfínteres'),
	('Se lleva bien con niños', 'Se lleva bien con niños'),
	('Es tímido', 'Es tímido'),
	('Inmaduro', 'Inmaduro'),
	('Impulsivo', 'Impulsivo'),
	('Hace rabietas', 'Hace rabietas'),
	('Comportamiento extraño', 'Comportamiento extraño'),
	('Problemas del sueño', 'Problemas del sueño'),
	('Tiene ausencias', 'Tiene ausencias'),
	('Tics o movimientos bruscos', 'Tics o movimientos bruscos'),
	('Independencia acorde a su edad', 'Independencia acorde a su edad'),
	('Conducta agresiva', 'Conducta agresiva'),
	('Rebeldia', 'Rebeldia'),
	('Mas activo que otros niños', 'Mas activo que otros niños'),
	('Conductas de riesgo', 'Conductas de riesgo'),
	('Conflictos con la ley', 'Conflictos con la ley'),
	('Consumo de sustancias', 'Consumo de sustancias'),
	('Dificultades en relaciones', 'Dificultades en relaciones'), 
	)


HISTORIA_MEDICA_CHOICES = (
	('Lesiones en la cabeza','Lesiones en la cabeza'),
	('Infecciones de oido','Infecciones de oido'),
	('Dificultades visuales','Dificultades visuales'),
	('Hospitalizaciones','Hospitalizaciones'),
	('Convulsiones','Convulsiones'),
	('Problemas emocionales','Problemas emocionales'),
	('Problemas de adaptacion','Problemas de adaptacion'),
	('Problemas de conducta','Problemas de conducta'),
	('Padeció meningitis o encefalitis','Padeció meningitis o encefalitis'),
	('Asma','Asma'),
	('Diabetes','Diabetes'),
	('Retraso de crecimiento','Retraso de crecimiento'),
	('Alergias','Alergias'),
	('Ha recibido tratamiento psicologico psiquiatrico','Ha recibido tratamiento psicologico psiquiatrico'),
	('Se queja del dolor de cabeza','Se queja del dolor de cabeza'),
	('Se queja del dolor de estomago','Se queja del dolor de estomago'),
	('Cirugias','Cirugias'),
	('Problemas en la alimentacion','Problemas en la alimentacion'),
	('Problemas de tiroides','Problemas de tiroides'),
	('Historia cardiovascular','Historia cardiovascular'),
)

HISTORIA_ESCOLAR_CHOICES = (

	('Dificultad en adaptacion', 'Dificultad en adaptacion'),
	('Dificultad en Socializacion', 'Dificultad en Socializacion'),
	('Necesidad de apoyo adicional', 'Necesidad de apoyo adicional'),
	('Deserción escolar', 'Deserción escolar'),
	('Dificultades en aprendizaje de lectura', 'Dificultades en aprendizaje de lectura'),
	('Dificultades en aprendizaje de escritura', 'Dificultades en aprendizaje de escritura'),
	('Dificultades en aprendizaje de aritmética', 'Dificultades en aprendizaje de aritmética'),
	('Fracaso escolar', 'Fracaso escolar'),
)

HISTORIA_SOCIOFAMILIAR_CHOICES = (

	('Conflictos de pareja', 'Conflictos de pareja'),
	('Conflictos entre padres e hijos', 'Conflictos entre padres e hijos'),
	('Conflictos entre hermanos', 'Conflictos entre hermanos'),
	('Pérdidas o duelos', 'Pérdidas o duelos'),
	('Consumo de alcohol o spa', 'Consumo de alcohol o spa'),
	('Dificultades en manejo de autoridad', 'Dificultades en manejo de autoridad'),
	)

SERVICIOS_CHOICES = (

    ('Neuropsicologia','Neuropsicologia'),
    ('Fonoaudiologia','Fonoaudiologia'),
    ('Salud ocupacional','Salud ocupacional'),
    ('Psicologia','Psicologia'),
    ('Fisioterapia','Fisioterapia'),
    ('Valoracion integral','Valoracion integral'),
    ('Neurologia','Neurologia'),
    ('Terapia ocupacional','Terapia ocupacional'),
)

SEXO_CHOICES = (

    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

class HistoriaNiño(models.Model):

	tipo_identificacion = models.CharField(max_length=50, choices = TIPO_IDENTIFICACION)	
	identificacion = models.CharField(max_length=50)
	primer_nombre = models.CharField(max_length = 50)
	segundo_nombre = models.CharField(max_length = 50, blank=True)
	primer_apellido = models.CharField(max_length = 50)
	segundo_apellido = models.CharField(max_length = 50, blank= True)
	sexo = models.CharField(max_length = 1, choices = SEXO_CHOICES)
	lugar_nacimiento = models.CharField(max_length = 100)
	telefono = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 50)
	correo = models.EmailField(max_length = 50)
	eps = models.CharField(max_length=100, choices = EPS_CHOICES)
	fecha_ingreso=models.CharField(max_length=100)
	institucion_educativa = models.CharField(max_length=50)
	nivel_educativo = models.CharField(max_length=20,choices=NIVEL_EDUCATIVO)
	primer_nombre_madre = models.CharField(max_length=50, help_text="Primer Nombre")
	segundo_nombre_madre = models.CharField(max_length=50)
	primer_apellido_madre = models.CharField(max_length=50)
	segundo_apellido_madre = models.CharField(max_length=50)
	fecha_nacimiento_madre = models.CharField(max_length=100)
	ocupacion_madre = models.CharField(max_length=50)
	primer_nombre_padre = models.CharField(max_length=50)
	segundo_nombre_padre = models.CharField(max_length=50)
	primer_apellido_padre = models.CharField(max_length=50)
	segundo_apellido_padre = models.CharField(max_length=50)
	fecha_nacimiento_padre = models.CharField(max_length=100)
	ocupacion_padre = models.CharField(max_length=50)
	remitido_por = models.CharField(max_length=50)
	diagnostico_principal=models.TextField(max_length=100)
	diagnostico_secundario=models.TextField(max_length=100)
	motivo_consulta = models.TextField(max_length=100)
	servicio_solicitado = models.CharField(max_length=100, choices = SERVICIOS_CHOICES)
	antecedentes_embarazo=MultiSelectField(choices = ANTECEDENTES_EMBARAZO)
	causa_hospitalizacion=models.TextField(max_length=100)
	parto = MultiSelectField(choices = PARTO_CHOICES)
	sostuvo_la_cabeza=models.CharField(max_length=10, help_text="Meses")
	se_sento_solo=models.CharField(max_length=10, help_text="Meses")
	gateo=models.CharField(max_length=10, help_text="Meses")
	camino_sin_apoyo=models.CharField(max_length=10, help_text="Meses")
	dijo_las_primeras_palabras=models.CharField(max_length=10, help_text="Meses")
	dijo_frases_simples=models.CharField(max_length=10, help_text="Meses")
	se_expreso_sin_errores_fonologicos=models.CharField(max_length=10, help_text="Años")
	inicio_lecto_escritura=models.CharField(max_length=10, help_text="Años")
	frases_gramaticales =models.CharField(max_length=10, help_text="Años")
	medicamentos = models.TextField(max_length=200)
	descripcion_problema_socio = models.TextField(max_length=200)

	conducta = MultiSelectField(choices = CONDUCTA_CHOICES)
	historia_medica = MultiSelectField(choices=HISTORIA_MEDICA_CHOICES)
	historia_escolar = MultiSelectField(choices= HISTORIA_ESCOLAR_CHOICES)
	historia_socio_familiar = MultiSelectField(choices = HISTORIA_SOCIOFAMILIAR_CHOICES)

	def __str__(self):
		return self.tipo_identificacion

	def get_absolute_url(self):
		return reverse('nino-lista')



