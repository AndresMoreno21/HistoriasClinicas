from django.shortcuts import render
from .models import *
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .serializers import FisioSerializer
# Create your views here.


def base(request):
    return render(request, 'base.html')


def fisio_base(request):
    fisio = Fisioterapia.objects.all()
    context = {'fisio_list': fisio}
    return render(request, 'FisioterapiaBase.html', context)
    

class FisioCreate(CreateView):
    model = Fisioterapia
    template_name = 'FisioterapiaCreate.html'
    fields = '__all__'

class FisioUpdate(UpdateView):
	model = Fisioterapia
	template_name = 'FisioterapiaDetalles.html'
	fields= '__all__'
# Create your views here.

class FisioViewSet(viewsets.ModelViewSet):
    queryset = Fisioterapia.objects.all()
    serializer_class = FisioSerializer
