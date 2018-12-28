from django.db import models
from multiselectfield import MultiSelectField

from django.urls import reverse

# Create your models here.



AREA= (
		('Memoria','Memoria'),
		('Atencion','Atencion'),
		('Lenguaje','Lenguaje'),
		('Funciones ejectuvias','Funciones ejectuvias'),
		('Cordinacion perceptual','Cordinacion perceptual'),
		)	

PRUEBAS_NEUROPSICOLOGICAS = (
		('Escala Weschler','Escala Weschler'),
		('ENI','ENI'),
		('Luria inicial','Luria inicial'),
		('Banfe','Banfe'),
		('Winsconsin','Winsconsin'),
		)	


class Neuropsicologia(models.Model):

	
	pruebas_neuropsicologicas = MultiSelectField(choices = PRUEBAS_NEUROPSICOLOGICAS)
	resultados_de_la_evaluacion_neuropsicologica = models.TextField(max_length=200)
	diagnostico = models.TextField(max_length=200)
	plan_intervencion = MultiSelectField(choices= AREA)
	detalles_de_la_intervencion = models.TextField(max_length=500)
	evolucion = models.TextField(max_length=200)
	concepto = models.TextField(max_length=500)
	continuidad_del_tratamiento = models.BooleanField(default = False)
	valoracion_de_avance = MultiSelectField(choices = AREA)
	detalles_del_avance = models.TextField(max_length=500)

	def __str__(self):

		return  self.id

	def get_absolute_url(self):
		return reverse('neuro-lista')