from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from aperturaAdultos.models import * 
from .forms import AdultoForm
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy 

from rest_framework import viewsets
from .serializers import AdultosSerializer

from aperturaAdultos import forms

# Create your views here.

@login_required
def base(request):
    return render(request, 'baseAdmin.html')



@login_required
def adultos_base(request):
    adultos = AperturaAdultos.objects.all()
    context = {'adultos_list': adultos}
    return render(request, 'adultosBase.html', context)


class AdultoCreate(LoginRequiredMixin, CreateView):
    model = AperturaAdultos
    form_class = forms.AdultoForm
    template_name = 'adultoCreate.html'
    success_url = reverse_lazy('adulto-lista')

class AdultoUpdate(LoginRequiredMixin,UpdateView):
    model = AperturaAdultos
    form_class = forms.AdultoForm
    template_name = 'adultoDetalles.html'
    success_url = reverse_lazy('adulto-lista')

class AdultoDelete(LoginRequiredMixin,DeleteView):
    model = AperturaAdultos
    template_name = 'aperturaadultos_confirm_delete.html'
    success_url = reverse_lazy('adulto-lista')

class AdultosViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = AperturaAdultos.objects.all()
    
    serializer_class = AdultosSerializer





