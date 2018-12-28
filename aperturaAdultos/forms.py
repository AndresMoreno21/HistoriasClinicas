from django import forms
from .models import *


class AdultoForm(forms.ModelForm):
    class Meta:
        model = AperturaAdultos
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
            'remitido_por': forms.TextInput(attrs={'class':'form-control'}),

            'motivo_consulta': forms.Textarea(attrs={'class':'form-control'}),
            'medicamentos': forms.Textarea(attrs={'class':'form-control'}),
            'estado_actual_enfermedad': forms.Textarea(attrs={'class':'form-control'}),
            'tratamiendo_actual': forms.Textarea(attrs={'class':'form-control'}),
            'antecedentes': forms.Textarea(attrs={'class':'form-control'}),
            'diagnostico_actual': forms.Textarea(attrs={'class':'form-control'}),
            

            'servicio_solicitado' : forms.Select(attrs={'class':'selectpicker'}),
            'sexo' : forms.Select(attrs={'class':'selectpicker'}),
            'ingreso' : forms.DateInput(attrs={'class':'form-control datepicker' }),
            'eps_afiliada' : forms.Select(attrs={'class':'selectpicker'}),
            'nivel_educativo' : forms.Select(attrs={'class':'selectpicker'}),
         }

