from django.db import models

from django.urls import reverse

# Create your models here.
class Psiquiatria(models.Model):
	TIPO_TRATAMIENTO = (
		('PSICOLOGICO', 'Tratamiento Psicologico'),
		('PSIQUIATRICO', 'Tratamiento Psiquiatrico'),
		)

	
	fecha=models.DateField()
	tratamiento= models.CharField(max_length=20,choices=TIPO_TRATAMIENTO)
	motivo_consulta=models.TextField(max_length=200) 
	diagnostico_actual=models.TextField(max_length=100)
	miembro = models.ManyToManyField('Familiograma', through= 'FamiliogramaPsiquiatria')
	historia_personal=models.TextField(max_length=200)
	patologicos=models.CharField(max_length=30)
	quirurgicos=models.CharField(max_length=30)
	toxicos=models.CharField(max_length=30)
	alegicos=models.CharField(max_length=30)
	traumaticos=models.CharField(max_length=30)
	ocupacionales=models.CharField(max_length=40)
	antecedentes_familiares=models.CharField(max_length=50)
	revision_por_sistemas=models.CharField(max_length=30)
	examen_mental=models.CharField(max_length=30)
	analisis=models.CharField(max_length=30)
	diagnosticos=models.CharField(max_length=30)
	plan_de_manejo=models.TextField(max_length=200)
	recomendaciones=models.TextField(max_length=200)

	def __str__(self):
		return self.paciente

	def get_absolute_url(self):
		return reverse('psiquiatria-lista')



class Familiograma(models.Model):

	miembro=models.CharField(max_length=30)
	

	def __str__(self):
		return self.miembro 

class FamiliogramaPsiquiatria(models.Model):
	miembro = models.ForeignKey('Familiograma', on_delete= models.CASCADE )
	psiquaitria = models.ForeignKey('Psiquiatria', on_delete= models.CASCADE)
	edad = models.CharField(max_length=50)
	parentezco = models.CharField(max_length=50)
	escolaridad = models.CharField(max_length=50)
	ocupacion= models.CharField(max_length=50)
