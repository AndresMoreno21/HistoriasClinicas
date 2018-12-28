from django import forms
from .models import *


class MenorForm(forms.ModelForm):
    class Meta:
        model = HistoriaNiño
        fields= '__all__'
        widgets = {

            'identificacion': forms.TextInput(attrs={'class':'form-control'}),
            'primer_nombre': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_nombre': forms.TextInput(attrs={'class':'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'lugar_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'causa_hospitalizacion': forms.TextInput(attrs={'class':'form-control'}),
            'diagnostico_principal': forms.TextInput(attrs={'class':'form-control'}),
            'diagnostico_secundario': forms.TextInput(attrs={'class':'form-control'}),
            'remitido_por': forms.TextInput(attrs={'class':'form-control'}),
            'institucion_educativa': forms.TextInput(attrs={'class':'form-control'}),
            'primer_nombre_madre': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_nombre_madre': forms.TextInput(attrs={'class':'form-control'}),
            'primer_apellido_madre': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_apellido_madre': forms.TextInput(attrs={'class':'form-control'}),
            'ocupacion_madre': forms.TextInput(attrs={'class':'form-control'}),
            'primer_nombre_padre': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_nombre_padre': forms.TextInput(attrs={'class':'form-control'}),
            'primer_apellido_padre': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_apellido_padre': forms.TextInput(attrs={'class':'form-control'}),
            'ocupacion_padre': forms.TextInput(attrs={'class':'form-control'}),
            'sostuvo_la_cabeza': forms.TextInput(attrs={'class':'form-control'}),
	        'se_sento_solo': forms.TextInput(attrs={'class':'form-control'}),
	        'gateo': forms.TextInput(attrs={'class':'form-control'}),
	        'camino_sin_apoyo': forms.TextInput(attrs={'class':'form-control'}),
	        'dijo_las_primeras_palabras': forms.TextInput(attrs={'class':'form-control'}),
	        'dijo_frases_simples': forms.TextInput(attrs={'class':'form-control'}),
	        'se_expreso_sin_errores_fonologicos': forms.TextInput(attrs={'class':'form-control'}),	
            'inicio_lecto_escritura': forms.TextInput(attrs={'class':'form-control'}),
            'frases_gramaticales': forms.TextInput(attrs={'class':'form-control'}),                


            'motivo_consulta': forms.Textarea(attrs={'class':'form-control'}),
            'descripcion_problema_socio': forms.Textarea(attrs={'class':'form-control'}),
            'medicamentos': forms.Textarea(attrs={'class':'form-control'}),
            'estado_actual_enfermedad': forms.Textarea(attrs={'class':'form-control'}),
            'tratamiendo_actual': forms.Textarea(attrs={'class':'form-control'}),
            'antecedentes': forms.Textarea(attrs={'class':'form-control'}),
            'diagnostico_actual': forms.Textarea(attrs={'class':'form-control'}),
            
            'tipo_identificacion': forms.Select(attrs={'class':'selectpicker'}),
            'servicio_solicitado' : forms.Select(attrs={'class':'selectpicker'}),
            'sexo' : forms.Select(attrs={'class':'selectpicker'}),
            'eps' : forms.Select(attrs={'class':'selectpicker'}),
            'nivel_educativo' : forms.Select(attrs={'class':'selectpicker'}),

            'fecha_nacimiento_madre' : forms.DateInput(attrs={'class':'form-control datepicker' }),
            'fecha_nacimiento_padre' : forms.DateInput(attrs={'class':'form-control datepicker' }),
            'fecha_ingreso' : forms.DateInput(attrs={'class':'form-control datepicker' }),
         }
        