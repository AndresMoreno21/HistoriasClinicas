from django.shortcuts import render
from Fonoaudiologia.models import Fonoaudiologia
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .serializers import FonoSerializer

# Create your views here.

def fono_base(request):
    fono = Fonoaudiologia.objects.all()
    context = {'fono_list': fono}
    return render(request, 'fonoaudiologia.html', context) 

class FonoCreate(CreateView):
    model = Fonoaudiologia
    template_name = 'fonoCreate.html'
    fields = '__all__'

class FonoUpdate(UpdateView):
	model = Fonoaudiologia
	template_name = 'fonoDetales.html'
	fields= '__all__'

class FonoViewSet(viewsets.ModelViewSet):
    queryset = Fonoaudiologia.objects.all()
    serializer_class = FonoSerializer
