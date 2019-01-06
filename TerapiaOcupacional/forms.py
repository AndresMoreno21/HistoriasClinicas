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
            'descripcion_movimientos_activos_y_pasivos': forms.Textarea(attrs={'class':'form-control'}),

            'cintura_escapular': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_cintura_escapular': forms.Textarea(attrs={'class':'form-control'}),

            'cadera': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_cadera': forms.Textarea(attrs={'class':'form-control'}),

            'rodilla': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_rodilla': forms.Textarea(attrs={'class':'form-control'}),

            'pie': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_pie': forms.Textarea(attrs={'class':'form-control'}),

            'deformaciones': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_deformaciones': forms.Textarea(attrs={'class':'form-control'}),

            'tono_muscular': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_tono_muscular': forms.Textarea(attrs={'class':'form-control'}),

            'actividad_refleja': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_actividad_refleja': forms.Textarea(attrs={'class':'form-control'}),

            'trofismo': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_trofismo': forms.Textarea(attrs={'class':'form-control'}),

            'funcion_muscular': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_funcion_muscular': forms.Textarea(attrs={'class':'form-control'}),

            'funcion_postural': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_funcion_postural': forms.Textarea(attrs={'class':'form-control'}),

            'tactil': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_tactil': forms.Textarea(attrs={'class':'form-control'}),

            'propioceptivo': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_propioceptivo': forms.Textarea(attrs={'class':'form-control'}),

            'vestibular': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_vestibular': forms.Textarea(attrs={'class':'form-control'}),

            'auditivo': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_auditivo': forms.Textarea(attrs={'class':'form-control'}),

            'gustativo': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_gustativo': forms.Textarea(attrs={'class':'form-control'}),

            'visual': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_visual': forms.Textarea(attrs={'class':'form-control'}),

            'olfativo': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_olfativo': forms.Textarea(attrs={'class':'form-control'}),

            'alimentacion': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_alimentacion': forms.Textarea(attrs={'class':'form-control'}),

            'higiene': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_higiene': forms.Textarea(attrs={'class':'form-control'}),

            'vestido': forms.Select(attrs={'class':'selectpicker'}),
            'descripcion_vestido': forms.Textarea(attrs={'class':'form-control'}),

            'descanso': forms.TextInput(attrs={'class':'form-control'}),
            'educacion': forms.TextInput(attrs={'class':'form-control'}),
            'juego': forms.TextInput(attrs={'class':'form-control'}),
            'otras': forms.Textarea(attrs={'class':'form-control'}),

            }
