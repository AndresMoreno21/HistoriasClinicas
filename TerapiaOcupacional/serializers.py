from .models import TerapiaOcupacional
from rest_framework import serializers

class TerapiaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TerapiaOcupacional 
		fields = ('__all__')
