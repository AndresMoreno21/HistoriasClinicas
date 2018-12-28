from django.db import models

from django.urls import reverse
from multiselectfield import MultiSelectField

NARIZ_FRENTE = (
		('NORMAL', 'Normal'),
		('DER', 'Desviada Derecha'),
		('IZQ', 'Desviada Izquierda'),
		)

NARIZ_INFERIOR = (
		('NORMAL', 'Normal'),
		('DER', 'Mayor Derecha'),
		('IZQ', 'Mayor Izquierda'),
		)

PERMEABILIDAD=(
		('NARINA DER', 'Narina Dercha'),
		('NARINA IZQ', 'Narina Izquierda'),
		)

FUNCIONALIDAD=(
		('FUNCIONAL', 'Funcional'),
		('NO FUNCIONAL', 'No Funcional'),
		)

FRENILLO=(
		('NORMAL', 'Normal'),
		('CORTO', 'Corto'),
		('TRANSFIXIANTE', 'Transfixiante'),
		)

LABIO_INFERIOR=(
		('NORMAL','Normal'),
		('EVERTIDO','Evertido'),
		)
        
TAMAÑO_LENGUA=(
		('NORMAL','Normal'),
		('AUMENTADO','Aumentado'),
		)

PALADAR_DURO=(
		('NORMAL','Normal'),
		('ALTO','Alto'),
		('FISURADO','Fisurado'),
		('OPERADO','Operado'),
		)

PALADAR_BLANDO=(
		('NORMAL','Normal'),
		('FISURADO','Fisurado'),
		('OPERADO','Operado'),
		)

UVULA=(
		('NORMAL','Normal'),
		('BIFIDA','Bifida'),
		)

FRENILLO2=(
		('NORMAL','Normal'),
		('CORTO','Corto'),
		)

AMIGDALAS=(
		('NORMALES','Normales'),
		('AUMENTADAS_DER','Aumentadas Derecha'),
		('AUMENTADAS_IZQ','Aumentadas Izquierda'),
		('AUSENTES','Ausentes'),
		)

POSICION_LINGUAL=(
		('NORMAL','Normal'),
		('DESCENDIDA','Descendida'),
		('INTERPUESTA','Interpuesta'),
		)

CIERRE_LABIAL=(
		('PRESENTE','Presente'),
		('AUSENTE','Ausente'),
		('CON ESFUERZO','Con Esfuerzo'),
		)

TIPO_RESPIRACION=(
		('COSTODIA','Costodriafragmatico'),
		('COSTAL ALTO','Costal Alto'),
		('MIXTO','Mixto'),
		)

MODO_RESPIRACION=(
		('NASAL','Nasal'),
		('ORAL','Oral'),
		('MIXTO','Mixto'),
		)

EJECUCION_PRAXICA=(
		('NORMAL','Normal'),
		('DISMINUIDA','Disminuida'),
		('SIN MOVILIDAD','Sin Movilidad'),
		)

EVALUACION_INTRAORAL =(
		('Apertura Bucal Máxima','Apertura Bucal Máxima'),
		('Con lengua en la papila','Con lengua en la papila'),
		)

TAMAÑO=(
		('NORMAL','Normal'),
		('CORTO','Corto'),
		('FISURADO','Fisurado'),
		('OPERADO','Operado'),
		)

	
TIPO_MALOS=(
		('Succión digital','Succión digital'),
		('Onicofagia','Onicofagia'),
		('Mamadera','Mamadera'),
		('Chupete','Chupete'),
		('Succión de Labio','Succión de Labio'),
		('Succión de objetos','Succión de objetos'),
		)

PRAXIA_LABIAL=(
		('Protrusion de ambos labios','Protrusion de ambos labios'),
		('Distension de ambos labios','Distension de ambos labios'),
		('Desviacion de labios a comisura derecha','Desviacion de labios a comisura derecha'),
		('Desviación de labios a comisura izquierda','Desviación de labios a comisura izquierda'),
		('Retrusión labial sonora','Retrusión labial sonora'),
		('Vibración labial','Vibración labial'),
		('Inflar mejillas','Inflar mejillas'),
		)

PRAXIA_LINGUAL=(
		('Apex lingual recorre arcada dentaria superior','Apex lingual recorre arcada dentaria superior'),
		('Apex lingual recorre arcada dentaria inferior','Apex lingual recorre arcada dentaria inferior'),
		('Apex lingual recorre paladar duro','Apex lingual recorre paladar duro'),
		('Adosamiento lingual','Adosamiento lingual'),
		('Chasquido lingual','Chasquido lingual'),
		('Vibración áfona en el alvéolo','Vibración áfona en el alvéolo'),
		('Vibración lingual áfona entre los labios','Vibración lingual áfona entre los labios'),
		('Elevación lingual extraoral','Elevación lingual extraoral'),
		('Descenso lingual extraoral','Descenso lingual extraoral'),
		('Lateralización de apex lingual a la derecha','Lateralización de apex lingual a la derecha'),
		('Lateralización de apex lingual a la izquierda','Lateralización de apex lingual a la izquierda'),
		('Apex lingual empuja mejilla derecha','Apex lingual empuja mejilla derecha'),
		('Apex lingual empuja mejilla izquierda','Apex lingual empuja mejilla izquierda'),
		('Apex lingual bajo labio superior','Apex lingual bajo labio superior'),
		('Apex lingual bajo labio inferior','Apex lingual bajo labio inferior'),
		)

TIPO_EVALUACION=(
		('Bilabial','Bilabial'),
		('Labiodental','Labiodental'),
		('Post Dental Inf.','Post Dental Inf.'),
		('Post Dental superior','Post Dental superior'),
		('Alveolar','Alveolar'),
		('Palatal','Palatal'),
		('Velar','Velar'),
		('Comp.Lab.Inferior','Comp.Lab.Inferior'),
		('Interdental','Interdental'),
		('Retrocedido','Retrocedido'),
		)

NARIZ_PERFIL =(
		('Normal','Normal'),
		('Forma','Forma'),
		)

LABIO_INFERIOR =(
		('Normal','Normal'),
		('Evertido','Evertido'),
		)


# Create your models here.
class Fonoaudiologia(models.Model):

	
	nariz_frente=models.CharField(max_length=20,choices=NARIZ_FRENTE)
	nariz_perfil = models.CharField(max_length=20, choices = NARIZ_PERFIL)
	nariz_vista_inferior=models.CharField(max_length=20,choices=NARIZ_INFERIOR)
	permeabilidad=models.CharField(max_length=20,choices=PERMEABILIDAD)
	tamaño_labio_superior =models.CharField(max_length=100 , choices = TAMAÑO)
	funcionalidad_labio_superior =models.CharField(max_length=20,choices=FUNCIONALIDAD)
	frenillo_labio_superior =models.CharField(max_length=20,choices=FRENILLO)
	labio_inferior = models.CharField(max_length=20, choices = LABIO_INFERIOR)
	evaluacion_intraoral=models.CharField(max_length=30,choices=EVALUACION_INTRAORAL)
	maxilar_superior=models.CharField(max_length=20)
	maxilar_inferior=models.CharField(max_length=20)
	intermaxilar_sagital=models.CharField(max_length=20)
	intermaxilar_vertical=models.CharField(max_length=20)
	intermaxilar_Transversal=models.CharField(max_length=20)
	tamaño_lengua = models.CharField(max_length=20,choices=TAMAÑO_LENGUA)
	frenillo_lengua= models.CharField(max_length=20,choices=FRENILLO2)
	forma_paladar_duro=models.CharField(max_length=30,choices=PALADAR_DURO)
	forma_paladar_blando=models.CharField(max_length=30,choices=PALADAR_BLANDO)
	uvula=models.CharField(max_length=10,choices=UVULA)
	amigdalas=models.CharField(max_length=20,choices=AMIGDALAS)
	posicion_lingual=models.CharField(max_length=20,choices=POSICION_LINGUAL)
	cierre_labial=models.CharField(max_length=20,choices=CIERRE_LABIAL)
	tipo_respiracion=models.CharField(max_length=20,choices=TIPO_RESPIRACION)
	modo_respiracion=models.CharField(max_length=10,choices=MODO_RESPIRACION)
	malos_habitos = MultiSelectField(choices = TIPO_MALOS)
	ejecucion_praxica=models.CharField(max_length=10,choices=EJECUCION_PRAXICA)
	praxias_labiales= MultiSelectField(choices = PRAXIA_LABIAL)
	praxias_linguales= MultiSelectField(choices = PRAXIA_LINGUAL)
	bilabial = models.CharField(max_length=20, help_text="Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)")
	labiodental = models.CharField(max_length=20, help_text="Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)")
	post_dent_inf = models.CharField(max_length=20, help_text="Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)")
	post_dent_sup = models.CharField(max_length=20, help_text="Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)")
	alveolar = models.CharField(max_length=20, help_text="Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)")
	palatal = models.CharField(max_length=20, help_text="Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)")
	velar = models.CharField(max_length=20, help_text="Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)")
	comp_lab_inf = models.CharField(max_length=20, help_text="Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)")
	interdental = models.CharField(max_length=20, help_text="Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)")
	retrocedido = models.CharField(max_length=20, help_text="Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)")
	Omite = models.CharField(max_length=20, help_text="Digitar solo las letras que logra pronunciar bien (M,P,B,F,S,T,D,N,L,R,RR,Ñ,CH,Y,J,K,G)")
	observaciones=models.TextField(max_length=200)
	tratamieto=models.TextField(max_length=200)

	def get_absolute_url(self):
		return reverse('fono-lista')


