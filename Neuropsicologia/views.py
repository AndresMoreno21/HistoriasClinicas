from django.shortcuts import render
from .models import *
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .serializers import NeuroSerializer
# Create your views here.


def base(request):
    return render(request, 'base.html')


def neuro_base(request):
    neuro = Neuropsicologia.objects.all()
    context = {'neuro_list': neuro}
    return render(request, 'NeuropsicologiaBase.html', context)
    

class NeuroCreate(CreateView):
    model = Neuropsicologia
    template_name = 'NeuropsicologiaCreate.html'
    fields = '__all__'

class NeuroUpdate(UpdateView):
	model = Neuropsicologia
	template_name = 'NeuropsicologiaDetalles.html'
	fields= '__all__'

# Create your views here.
class NeuroViewSet(viewsets.ModelViewSet):
    queryset = Neuropsicologia.objects.all()
    serializer_class = NeuroSerializer
