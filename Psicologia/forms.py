from django import forms
from .models import *

class PsicologiaForm(forms.ModelForm):
    class Meta:
        model = Psicologia
        fields= '__all__'
        widgets = {

        'fecha': forms.DateInput(attrs={'class':'form-control datepicker' }),
        'motivo_consulta': forms.TextInput(attrs={'class':'form-control'}),
        'percepcion_paciente': forms.TextInput(attrs={'class':'form-control'}),
        'sintomas': forms.TextInput(attrs={'class':'form-control'}),
        'antecendentes_del_motivo_de_consulta': forms.TextInput(attrs={'class':'form-control'}),
        'historia_familiar_relevante': forms.TextInput(attrs={'class':'form-control'}),
        'historia_personal': forms.TextInput(attrs={'class':'form-control'}),
        'consumo_sustancias_psicoactivas': forms.TextInput(attrs={'class':'form-control'}),
        'tratamientos_psicologicos_o_psiquiatricos_previos': forms.TextInput(attrs={'class':'form-control'}),
        'antecedentes': forms.TextInput(attrs={'class':'form-control'}),
        'conflictos_intrapsiquicos': forms.TextInput(attrs={'class':'form-control'}),
        'expectativas_del_paciente': forms.TextInput(attrs={'class':'form-control'}),
        'factores_de_riesgo': forms.TextInput(attrs={'class':'form-control'}),
        'caracteristicas_cognitivas': forms.TextInput(attrs={'class':'form-control'}),
        'caracteristicas_sociales_y_relaciones_interpersonales': forms.TextInput(attrs={'class':'form-control'}),
        'caracteristicas_del_rango_afectivo_y_emocional': forms.TextInput(attrs={'class':'form-control'}),
        'caracteristicas_de_conducta': forms.TextInput(attrs={'class':'form-control'}),
        'caracteristicas_laborales': forms.TextInput(attrs={'class':'form-control'}),
        }


