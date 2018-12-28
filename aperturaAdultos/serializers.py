from .models import AperturaAdultos
from rest_framework import serializers

class AdultosSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AperturaAdultos
		fields = ('__all__')