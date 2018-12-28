from django.shortcuts import render
from .models import *
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from Psicologia import forms
from django.urls import reverse_lazy 
from .serializers import PsicoSerializer
# Create your views here.


def psico_base(request):
    psico = Psicologia.objects.all()
    context = {'psico_list': psico}
    return render(request, 'PsicologiaBase.html', context)
    

class PsicologiaCreate(LoginRequiredMixin,CreateView):
    model = Psicologia
    form_class = forms.PsicologiaForm
    template_name = 'PsicologiaCreate.html'
    success_url = reverse_lazy('psico-lista')



class PsicologiaUpdate(LoginRequiredMixin,UpdateView):
    model = Psicologia
    form_class = forms.PsicologiaForm
    template_name = 'PsicologiaDetalles.html'
    success_url = reverse_lazy('psico-lista')


class PsicoViewSet(viewsets.ModelViewSet):
    queryset = Psicologia.objects.all()
    serializer_class = PsicoSerializer



