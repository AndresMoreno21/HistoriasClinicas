from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from aperturaNinos.models import HistoriaNiño
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from rest_framework import viewsets
from .serializers import NiñoSerializer
from aperturaNinos import forms
from django.urls import reverse_lazy

# Create your views here.

@login_required
def niños_base(request):
    niños = HistoriaNiño.objects.all()
    context = {'niños_list': niños}
    return render(request, 'ninoBase.html', context)
    

class NiñoCreate(LoginRequiredMixin,CreateView):
    model = HistoriaNiño
    form_class = forms.MenorForm
    template_name = 'ninoCreate.html'
    success_url = reverse_lazy('nino-lista')

class NiñoUpdate(LoginRequiredMixin,UpdateView):
	model = HistoriaNiño
	template_name = 'ninoDetalles.html'
	fields= '__all__'


class NiñoDelete(LoginRequiredMixin, DeleteView):
    model = HistoriaNiño
    template_name = 'nino_confirm_delete.html'
    fields='__all__'


class Buscar(LoginRequiredMixin,TemplateView):
    
    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        id = HistoriaNiño.objects.filter(niño__contains=buscar)
        
        return render(request, 'buscarNiño.html' , {'id': id})


class NiñoViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    queryset = HistoriaNiño.objects.all()
    serializer_class = NiñoSerializer
