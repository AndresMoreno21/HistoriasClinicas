from .models import HistoriaNiño
from rest_framework import serializers

class NiñoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = HistoriaNiño 
		fields = ('__all__')