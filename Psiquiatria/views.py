from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from Psiquiatria.models import Psiquiatria
from rest_framework import viewsets
from .serializers import PsiquiatriaSerializer

# Create your views here.
def psiquiatria_base(request):
	psiquia = Psiquiatria.objects.all()
	context = {'psiquiatria_list': psiquia}
	return render(request, 'Psiquiatria/psiquiatria.html', context)

def psiquiatria_detail(request, psiquiatria_id):
	
	psiquiatria = Psiquiatria.objects.get(id=psiquiatria_id)
	context={'object':psiquiatria}
	return render(request,'Psiquiatria/psiquiatriaDetalles.html', context)

class PsiquiatriaCreate(CreateView):
	model = Psiquiatria
	fields = '__all__'

class PsiquiatriaUpdate(UpdateView):
	model = Psiquiatria
	fields= '__all__'

class PsiquiatriaDelete(DeleteView):
	model = Psiquiatria
	success_url = reverse_lazy('psiquiatria-lista')

class PsiquiatriaViewSet(viewsets.ModelViewSet):
    queryset = Psiquiatria.objects.all()
    serializer_class = PsiquiatriaSerializer