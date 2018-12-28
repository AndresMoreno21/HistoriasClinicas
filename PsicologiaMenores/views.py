from django.shortcuts import render
from .models import *
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from PsicologiaMenores import forms
from django.urls import reverse_lazy 

# Create your views here.


def base(request):
    return render(request, 'baseAdmin.html')


def psicoMenor_base(request):
    psicoMenor = PsicologiaMenores.objects.all()
    context = {'psicoMenor_list': psicoMenor}
    return render(request, 'PsicologiaMenorBase.html', context)
    


class PsicologiaMenorCreate(CreateView):
    model = PsicologiaMenores
    form_class = forms.PsicologiaMenorForm
    template_name = 'PsicologiaMenorCreate.html'
    success_url = reverse_lazy('psicoMenor-lista')

class PsicologiaMenorUpdate(UpdateView):
    model = PsicologiaMenores
    form_class = forms.PsicologiaMenorForm
    template_name = 'PsicologiaMenorDetalles.html'
    success_url = reverse_lazy('psicoMenor-lista')


