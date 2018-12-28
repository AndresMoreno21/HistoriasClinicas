from .models import Psiquiatria
from rest_framework import serializers

class PsiquiatriaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Psiquiatria
		fields = ('__all__')