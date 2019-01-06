from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from aperturaAdultos.models import AperturaAdultos
from aperturaNinos.models import HistoriaNiño

ALTERADO_NORMAL_CHOICES = (

    ('Normal', 'Normal'),
    ('Alterado', 'Alterado'),
)

SISTEMA_NEUROMUSCULAR_CHOICES = (

    ('Normal', 'Normal'),
    ('Hipertono', 'Hipertono'),
    ('Hipotono', 'Hipotono'),
)

SISTEMA_SENSORIAL_CHOICES = (
    ('Presentes', 'Presentes'),
    ('Ausentes', 'Ausentes'),
)

ACTIVIDADES_VIDA_DIARIA_CHOICES = (
    ('Sin Apoyo', 'Sin apoyo'),
    ('Con Apoyo', 'Con apoyo'),
)

PRUEBAS_APLICADAS_CHOICES = (
    ('COMPS', 'COMPS'),
    ('TEPSI', 'TEPSI'),
    ('OBSERVACIONES CLINCIAS I.S', 'OBSERVACIONES CLINCIAS I.S'),
    ('SIPT', 'SIPT'),
)

    
class TerapiaOcupacional(models.Model):
    
    pacienteAdulto = models.ForeignKey(AperturaAdultos, on_delete=models.CASCADE, blank=True , null=True)
    pacienteNiño = models.ForeignKey(HistoriaNiño, on_delete=models.CASCADE, blank=True , null=True)
    
    movimientos_activos_y_pasivos = models.CharField(max_length=20, choices = ALTERADO_NORMAL_CHOICES)
    descripcion_movimientos_activos_y_pasivos = models.TextField(max_length=2000, blank= True)

    cintura_escapular = models.CharField(max_length=20, choices = ALTERADO_NORMAL_CHOICES, help_text = "Hombros")
    descripcion_cintura_escapular = models.TextField(max_length=2000, blank= True)

    cadera = models.CharField(max_length=20, choices = ALTERADO_NORMAL_CHOICES, help_text = "Pelvis")
    descripcion_cadera = models.TextField(max_length=2000, blank= True)

    rodilla = models.CharField(max_length=20, choices = ALTERADO_NORMAL_CHOICES , help_text = "Genu varus, genu valgus , movilidad, crujidos articulares.")
    descripcion_rodilla = models.TextField(max_length=2000, blank= True)

    pie = models.CharField(max_length=20, choices = ALTERADO_NORMAL_CHOICES, help_text="Equinus, talus, varus, valgus, planos, hallux valgus")
    descripcion_pie = models.TextField(max_length=2000, blank= True)

    deformaciones = models.CharField(max_length=20, choices = ALTERADO_NORMAL_CHOICES, help_text="Cifosis, lordosis, escoliosis, cifoescoliosis.")
    descripcion_deformaciones = models.TextField(max_length=2000, blank= True)

    tono_muscular = models.CharField(max_length=20, choices = SISTEMA_NEUROMUSCULAR_CHOICES)
    actividad_refleja = models.CharField(max_length=20, choices = SISTEMA_NEUROMUSCULAR_CHOICES)
    
    trofismo = models.CharField(max_length=2000, blank= True, choices = ALTERADO_NORMAL_CHOICES)
    descripcion_trofismo = models.TextField(max_length=2000, blank= True)

    funcion_muscular = models.CharField(max_length=2000, blank= True, choices = ALTERADO_NORMAL_CHOICES)
    descripcion_funcion_muscular = models.TextField(max_length=2000, blank= True)

    funcion_postural = models.CharField(max_length=2000, blank= True, choices = ALTERADO_NORMAL_CHOICES)
    descripcion_funcion_postural = models.TextField(max_length=2000, blank= True)

    tactil = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    descripcion_tactil = models.TextField(max_length=2000, blank= True)

    propioceptivo = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    descripcion_propioceptivo = models.TextField(max_length=2000, blank= True)

    vestibular = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    descripcion_vestibular = models.TextField(max_length=2000, blank= True)

    auditivo = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    descripcion_auditivo = models.TextField(max_length=2000, blank= True)

    gustativo = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    descripcion_gustativo = models.TextField(max_length=2000, blank= True)

    visual = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    descripcion_visual = models.TextField(max_length=2000, blank= True)

    olfativo = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    descripcion_olfativo = models.TextField(max_length=2000, blank= True)

    alimentacion = models.CharField(max_length=100, choices = ACTIVIDADES_VIDA_DIARIA_CHOICES)
    descripcion_alimentacion = models.TextField(max_length=2000, blank= True)

    higiene =  models.CharField(max_length=100, choices = ACTIVIDADES_VIDA_DIARIA_CHOICES)
    descripcion_higiene = models.TextField(max_length=2000, blank= True)

    vestido = models.CharField(max_length=100, choices = ACTIVIDADES_VIDA_DIARIA_CHOICES)
    descripcion_vestido = models.TextField(max_length=2000, blank= True)

    descanso = models.TextField(max_length=500)
    educacion = models.TextField(max_length=500)
    juego = models.TextField(max_length=500)
    pruebas_aplicadas = MultiSelectField(max_length=100, choices = PRUEBAS_APLICADAS_CHOICES)
    otras = models.TextField(max_length= 300 , blank = True)

    def __str__(self):
        return self.id