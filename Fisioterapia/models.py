from django.db import models

from multiselectfield import MultiSelectField
from django.urls import reverse
# Create your models here.

INGRESO = (
    ('Solo','Solo'),
    ('Acompañado','Acompañado'),
    ('Ayudas externas','Ayudas externas'),

)

DOLOR = (
        ('Agudo','Agudo'),
        ('Subagudo','Subagudo'),
        ('Cronico','Cronico'),
        ('Ninguno','Ninguno'),
        
    )

EAV = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    )

IZQ_DER = (
    ('Derecha','Derecha'),
    ('Izquierda','Izquierda'),
    
)

TIPO_FUNCIONALIDAD = (
    ('Normal','Normal'),
    ('Alterada','Alterada'),
    
)

CHOICE_GRADO =(
        ('Primer Grado','Primer Grado'),
        ('Segundo Grado','Segundo Grado'),
        ('Tercer Grado','Tercer Grado'),
    )

HABITOS_SALUD = (
        ('El paciente fuma','El paciente fuma'),
        ('Paciente exfumador','Paciente exfumador'),
        ('Bebedor habitula','Bebedor habitual'),
        ('Realiza ejercicio','Realiza ejercicio'),
    
    )

TIPO_DOLOR = (
        ('Punzante','Punzante'),
        ('Irritante','Irritante'),
        ('Quemante','Quemante'),
        
    )

TIPO_MORFOLOGICO = (
        ('Mixto + Anterior','Mixto + Anterior'),
        ('Mixto + Posterior','Mixto + Posterior'),
        
    )

RECOM_CASERAS = (
        ('VERBALES','VERBALES'),
        ('PLAN CASERO','PLAN CASERO'),
        
    )

DESEQUILIBRIO = (
        ('Desequilibrio Posterior','Desequilibrio Posterior'),
        ('Desequilibrio Anterioir','Desequilibrio Anterior'),
        ('Desequilibrio Mixto','Desequilibrio Mixto'),        
        ('Desequilibrio + Anterior','Desequilibrio + Anterior'),
        ('Desequilibrio + Posterior','Desequilibrio + Posterior'),
        
    )

class Fisioterapia(models.Model):

    
    enfermedades_previas = models.TextField(max_length=200)
    otras_enfermedades = models.TextField(max_length=200)
    patologia_familiar = models.TextField(max_length = 500 , default = "ENFERMEDAD:                    | GRADO DE CONSANGUINEIDAD:         ")
    sintomas = models.CharField(max_length= 200 , help_text = "Del ultimo año")
    Otros_sintomas = models.TextField(max_length=500)
    intervenciones_quirurgicas = models.TextField(max_length=500)
    fechas_de_la_intervencion = models.TextField(max_length=500)
    tipo_de_intervencion = models.TextField(max_length=200)
    embarazo = models.BooleanField(default = False)
    tratamientos_previos = models.TextField(max_length=500, help_text = "Para el tratamiento actual")
    encontro_mejoria = models.BooleanField(default = False)
    otros_tratamientos = models.TextField(max_length=500)
    descripcion_del_proceso_actual = models.TextField(max_length=500)
    expectativas_del_paciente = models.TextField(max_length=500)
    expectativas_de_la_familia = models.TextField(max_length=500)
    datos_de_interes = models.TextField(max_length=500)
    habitos_de_salud = MultiSelectField(choices = HABITOS_SALUD)
    peso = models.IntegerField()
    talla = models.IntegerField()
    indice_de_masa_corporal = models.IntegerField()
    exploraciones_complementarias = models.TextField(max_length=200)
    hallazgos_relevantes = models.TextField(max_length=200)
    preescripciones_para_el_tratamiento_actual = models.TextField(max_length=200)
    automedicaciones = models.TextField(max_length=200)
    otras_medicaciones = models.TextField(max_length=200, blank = True)
    especificaciones_de_la_medicacion = models.TextField(max_length=200)
    el_paciente_vive_con = models.TextField(max_length=200)
    situacion_laboral = models.TextField(max_length=200)
    acceso_de_vivienda = models.TextField(max_length=200, help_text="¿Para acceder a la vivienda habitual de quien depende?")
    ayudas_tecnicas = models.TextField(max_length=200)
    dificultades = models.TextField(max_length=200)
    dicultad_en_el_autocuidado = models.TextField(max_length=200)
    dificultad_en_las_actividades_del_hogar = models.TextField(max_length=200)
    dificultad_en_las_actividades_sociales = models.TextField(max_length=200)
    ingreso = models.CharField(max_length=50, choices = INGRESO)
    dolor = models.CharField(max_length = 50 , choices = DOLOR) 
    localizacion = models.CharField(max_length=100)
    factor_desencadenante = models.TextField(max_length=200)
    tipo_de_dolor = MultiSelectField(choices = TIPO_DOLOR)
    EAV = models.CharField(max_length=100 , choices= EAV)
    resultados = models.TextField(max_length=200)
    tipo_morfologico = MultiSelectField( choices = TIPO_MORFOLOGICO)
    desequilibrio = MultiSelectField(choices = DESEQUILIBRIO)
    SHOUARD = models.CharField(max_length=50, choices = IZQ_DER)
    ECOM = models.CharField(max_length=50, choices = IZQ_DER)
    musculos_afectados = models.TextField(max_length=200)
    escoliosis = models.BooleanField(default= False)
    componente_rotacional = models.BooleanField(default= False)
    EDEMA = models.TextField(max_length=200)
    bandas_palpables = models.TextField(max_length=200)
    fascinas_adheridas = models.BooleanField(default = False)
    puntos_gatillos =  models.BooleanField(default = False)
    puntos_dolorosos =  models.BooleanField(default = False)
    confractura_muscular =  models.BooleanField(default = False)
    retraccion_muscular = models.TextField(max_length=200, help_text="especifica Y/O Neuromeningeas")
    amplitud_articular = models.TextField(max_length=500, default="SEGMENTO ARTICULAR | MOVIMIENTO | GRADO ")
    sensibilidad_superficial = models.TextField(max_length=200)
    fuerza_muscular = models.TextField(max_length=200)
    tipo_de_funcionalidad = models.CharField(max_length= 100, choices= TIPO_FUNCIONALIDAD)
    equilibrio_y_reacciones_de_enderezamiento = models.TextField(max_length=200)
    propiocepcion = models.TextField(max_length=200)
    miembros_superiores = models.IntegerField()
    miembros_inferiores = models.IntegerField()
    Columna = models.IntegerField()
    diagnostico = models.TextField(max_length=200)
    intervencion_fisioterapeutica = models.TextField(max_length=500)
    recomendaciones_caseras = MultiSelectField(choices = RECOM_CASERAS)
    resultados = models.CharField(max_length= 100)
    sesiones_autorizadas = models.IntegerField()
    sesiones_realizadas = models.IntegerField()
    inasistencias = models.IntegerField()
    escala_funcional_final = models.IntegerField()
    definicion_de_manejo = models.TextField(max_length=200)
    evolucion = models.TextField(max_length=800)

    def get_absolute_url(self):
        return reverse('fisio-lista')