from django.shortcuts import render
from TerapiaOcupacional.models import TerapiaOcupacional
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from TerapiaOcupacional import forms
from rest_framework import viewsets
from .serializers import TerapiaSerializer

@login_required
def terapia_base(request):
	tera = TerapiaOcupacional.objects.all()
	context = {'terapia_list': tera}
	return render(request, 'TerapiaOcupacional/terapia.html', context)

class TerapiaCreate(LoginRequiredMixin,CreateView):
	model = TerapiaOcupacional
	form_class = forms.TerapiaForm
	template_name = 'TerapiaOcupacional/terapiaocupacional_form.html'
	success_url = reverse_lazy('terapia-lista')

class TerapiaUpdate(LoginRequiredMixin,UpdateView):
	model = TerapiaOcupacional
	form_class = forms.TerapiaForm
	template_name = 'TerapiaOcupacional/terapiaDetalles.html'
	success_url = reverse_lazy('terapia-lista')

class TerapiaDelete(LoginRequiredMixin,DeleteView):
	model = TerapiaOcupacional
	success_url = reverse_lazy('terapia-lista')

class TerapiaViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    queryset = TerapiaOcupacional.objects.all()
    serializer_class = TerapiaSerializer

