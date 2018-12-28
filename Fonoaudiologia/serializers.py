from .models import Fonoaudiologia
from rest_framework import serializers

class FonoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fonoaudiologia
		fields = ('__all__')