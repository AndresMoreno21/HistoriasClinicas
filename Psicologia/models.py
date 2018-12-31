from django.db import models
from django.urls import reverse
from aperturaAdultos.models import AperturaAdultos



class Psicologia(models.Model):    
    
    pacienteAdulto = models.ForeignKey(AperturaAdultos, on_delete=models.CASCADE)
    percepcion_paciente = models.TextField(max_length=500)
    sintomas = models.TextField(max_length=500)
    antecendentes_del_motivo_de_consulta = models.TextField(max_length=500)
    historia_familiar_relevante = models.TextField(max_length=500)
    historia_personal = models.TextField(max_length=500 , help_text="Desarrollo relevante.")
    consumo_sustancias_psicoactivas = models.TextField(max_length=500)
    tratamientos_psicologicos_o_psiquiatricos_previos = models.TextField(max_length=500)
    antecedentes = models.TextField(max_length=500, help_text="Antecedentes de tipo psicologico, psiquiatricos y medicos familiares.")
    conflictos_intrapsiquicos = models.TextField(max_length=500)
    expectativas_del_paciente = models.TextField(max_length=500)
    factores_de_riesgo = models.TextField(max_length=500 , help_text="Factores de riesgo, protectores y predisponentes")
    caracteristicas_cognitivas = models.TextField(max_length=500)
    caracteristicas_sociales_y_relaciones_interpersonales = models.TextField(max_length=500)
    caracteristicas_del_rango_afectivo_y_emocional = models.TextField(max_length=500)
    caracteristicas_de_conducta = models.TextField(max_length=500)
    caracteristicas_laborales = models.TextField(max_length=500)

    def get_absolute_url(self):
        return reverse('psico-lista')

    def __str__(self):
        return self.Historia_No





