from .models import Neuropsicologia
from rest_framework import serializers

class NeuroSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Neuropsicologia 
		fields = ('__all__')