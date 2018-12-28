from .models import Fisioterapia
from rest_framework import serializers

class FisioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fisioterapia 
		fields = ('__all__')