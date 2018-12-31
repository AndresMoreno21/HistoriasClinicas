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
    cintura_escapular = models.CharField(max_length=20, choices = ALTERADO_NORMAL_CHOICES, help_text = "Hombros")
    cadera = models.CharField(max_length=20, choices = ALTERADO_NORMAL_CHOICES, help_text = "Pelvis")
    rodilla = models.CharField(max_length=20, choices = ALTERADO_NORMAL_CHOICES , help_text = "Genu varus, genu valgus , movilidad, crujidos articulares.")
    pie = models.CharField(max_length=20, choices = ALTERADO_NORMAL_CHOICES, help_text="Equinus, talus, varus, valgus, planos, hallux valgus")
    deformaciones = models.CharField(max_length=20, choices = ALTERADO_NORMAL_CHOICES, help_text="Cifosis, lordosis, escoliosis, cifoescoliosis.")

    tono_muscular = models.CharField(max_length=20, choices = SISTEMA_NEUROMUSCULAR_CHOICES)
    actividad_refleja = models.CharField(max_length=20, choices = SISTEMA_NEUROMUSCULAR_CHOICES)
    
    trofismo = models.CharField(max_length=200, choices = ALTERADO_NORMAL_CHOICES)
    funcion_muscular = models.CharField(max_length=200, choices = ALTERADO_NORMAL_CHOICES)
    funcion_postural = models.CharField(max_length=200, choices = ALTERADO_NORMAL_CHOICES)
    tactil = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    propioceptivo = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    vestibular = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    auditivo = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    gustativo = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    visual = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    olfativo = models.CharField(max_length=100, choices = SISTEMA_SENSORIAL_CHOICES)
    alimentacion = models.CharField(max_length=100, choices = ACTIVIDADES_VIDA_DIARIA_CHOICES)
    higiene =  models.CharField(max_length=100, choices = ACTIVIDADES_VIDA_DIARIA_CHOICES)
    vestido = models.CharField(max_length=100, choices = ACTIVIDADES_VIDA_DIARIA_CHOICES)
    descanso = models.TextField(max_length=500)
    educacion = models.TextField(max_length=500)
    juego = models.TextField(max_length=500)
    pruebas_aplicadas = MultiSelectField(max_length=100, choices = PRUEBAS_APLICADAS_CHOICES)
    otras = models.TextField(max_length= 200 , blank = True)

    def __str__(self):
        return self.paciente