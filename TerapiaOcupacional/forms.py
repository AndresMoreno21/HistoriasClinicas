from django import forms
from .models import *

class TerapiaForm(forms.ModelForm):
    class Meta:
        model = TerapiaOcupacional
        fields= '__all__'
        widgets = {
            'pacienteAdulto': forms.Select(attrs={'class':'selectpicker'}),
            'pacienteNiño': forms.Select(attrs={'class':'selectpicker'}),
            'movimientos_activos_y_pasivos': forms.Select(attrs={'class':'selectpicker'}),
            'cintura_escapular': forms.Select(attrs={'class':'selectpicker'}),
            'cadera': forms.Select(attrs={'class':'selectpicker'}),
            'rodilla': forms.Select(attrs={'class':'selectpicker'}),
            'pie': forms.Select(attrs={'class':'selectpicker'}),
            'deformaciones': forms.Select(attrs={'class':'selectpicker'}),
            'tono_muscular': forms.Select(attrs={'class':'selectpicker'}),
            'actividad_refleja': forms.Select(attrs={'class':'selectpicker'}),
            'trofismo': forms.Select(attrs={'class':'selectpicker'}),
            'funcion_muscular': forms.Select(attrs={'class':'selectpicker'}),
            'funcion_postural': forms.Select(attrs={'class':'selectpicker'}),
            'tactil': forms.Select(attrs={'class':'selectpicker'}),
            'propioceptivo': forms.Select(attrs={'class':'selectpicker'}),
            'vestibular': forms.Select(attrs={'class':'selectpicker'}),
            'auditivo': forms.Select(attrs={'class':'selectpicker'}),
            'gustativo': forms.Select(attrs={'class':'selectpicker'}),
            'visual': forms.Select(attrs={'class':'selectpicker'}),
            'olfativo': forms.Select(attrs={'class':'selectpicker'}),
            'alimentacion': forms.Select(attrs={'class':'selectpicker'}),
            'higiene': forms.Select(attrs={'class':'selectpicker'}),
            'vestido': forms.Select(attrs={'class':'selectpicker'}),
            'descanso': forms.TextInput(attrs={'class':'form-control'}),
            'educacion': forms.TextInput(attrs={'class':'form-control'}),
            'juego': forms.TextInput(attrs={'class':'form-control'}),
            'otras': forms.Textarea(attrs={'class':'form-control'}),
            }
