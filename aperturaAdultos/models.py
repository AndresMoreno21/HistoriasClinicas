from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField


HISTORIA_MEDICA_CHOICES = (
    ('Lesiones en la cabeza','Lesiones en la cabeza'),
    ('Dificultades auditivas','Dificultades auditivas'),
    ('Dificultades visuales','Dificultades visuales'),
    ('Hospitalizaciones','Hospitalizaciones'),
    ('Convulsiones','Convulsiones'),
    ('Problemas emocionales','Problemas emocionales'),
    ('Problemas de conducta','Problemas de conducta'),
    ('Trastornos de alimentacion','Trastornos de alimentacion'),
    ('Accidentes','Accidentes'),
    ('Alteraciones dermatologicas','Alteraciones dermatologicas'),
    ('Alergias','Alergias'),
    ('Ha recibido tratamiento psicologico psiquiatrico','Ha recibido tratamiento psicologico psiquiatrico'),
    ('Cefaleas','Cefaleas'),
    ('Afecciones gastrointestinales','Afecciones gastrointestinales'),
    ('Afecciones osteomusculares','Afecciones osteomusculares'),
    ('Afecciones respiratorias','Afecciones respiratorias'),
    ('Trastornos neuromotores','Trastornos neuromotores'),
    ('Afeccion cardiaca','Afeccion cardiaca'),
    ('Problemas de tiroides','Problemas de tiroides'),
    ('Diabetes','Diabetes'),

)

HABITOS_CHOICES = (

    ('Deportes o actividad fisica', 'Deportes o actividad fisica'),
    ('Consumo de cigarrillo, alcohol, otras sustancias', 'Consumo de cigarrillo, alcohol, otras sustancias'),
    ('Factores estresantes', 'Factores estresantes'),
    ('Actividades recreativas', 'Actividades recreativas'),
   
)

AREA_CHOICES = (

    ('Actualmente tiene vinculación laboral', 'Actualmente tiene vinculación laboral'),
    ('Satisfacción laboral', 'Satisfacción laboral'),
    ('Dificultades en el desempeño laboral u ocupacional', 'Dificultades en el desempeño laboral u ocupacional'),
    ('Presencia de estrés laboral', 'Presencia de estrés laboral'),
    
)

SOCIO_CHOICES = (

    ('Conflictos de pareja', 'Conflictos de pareja'),
    ('Conflictos entre padres e hijos', 'Conflictos entre padres e hijos'),
    ('Conflictos entre hermanos', 'Conflictos entre hermanos'),
    ('Red de apoyo ', 'Red de apoyo '),
    ('Pérdidas o duelos', 'Pérdidas o duelos'),
    ('Consumo de alcohol o spa', 'Consumo de alcohol o spa'),
    ('Situaciones estresantes', 'Situaciones estresantes'),
    ('Cuidador', 'Cuidador'),
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

NIVEL_EDUCATIVO_CHOICES = (

    ('Ninguno', 'Ninguno'),
    ('Primaria', 'Primaria'),
    ('Bachiller', 'Bachiller'),
    ('Tecnico/Tecnologo', 'Tecnico/Tecnologo'),
    ('Profesional', 'Profesional'),
    ('Profesional Especialista', 'Profesional Especialista'),
    ('Profesional Magister', 'Profesional Magister'),
    ('Estudios Avanzados', 'Estudios Avanzados'),
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

class AperturaAdultos(models.Model):

    identificacion = models.CharField(max_length = 100)
    
    primer_nombre = models.CharField(max_length = 50)
    segundo_nombre = models.CharField(max_length = 50, blank=True)
    primer_apellido = models.CharField(max_length = 50)
    segundo_apellido = models.CharField(max_length = 50, blank= True)
    sexo = models.CharField(max_length = 1, choices = SEXO_CHOICES)
    lugar_nacimiento = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 50)
    correo = models.EmailField(max_length = 50)
    remitido_por = models.CharField(max_length = 50)
    motivo_consulta = models.TextField(max_length=500)
    medicamentos = models.TextField(max_length=100)
    servicio_solicitado = models.CharField(max_length=100, choices = SERVICIOS_CHOICES)
    eps_afiliada = models.CharField(max_length=100, choices = EPS_CHOICES)
    ingreso = models.CharField(max_length=100)
    nivel_educativo = models.CharField(max_length = 100, choices = NIVEL_EDUCATIVO_CHOICES)
    historias_medicas = MultiSelectField(choices = HISTORIA_MEDICA_CHOICES)
    diagnostico_actual = models.TextField(max_length=500)
    estado_actual_enfermedad = models.TextField(max_length=500)
    tratamiendo_actual = models.TextField(max_length=500)
    antecedentes = models.TextField(max_length=500)
    habitos_estilo_vida = MultiSelectField(choices = HABITOS_CHOICES)
    area_labor = MultiSelectField(choices = AREA_CHOICES)
    sociofamiliar = MultiSelectField(choices = SOCIO_CHOICES)
    
    

    def get_absolute_url(self):
        return reverse('adulto-lista')
        

    def __str__(self):
        return self.identificacion


    
