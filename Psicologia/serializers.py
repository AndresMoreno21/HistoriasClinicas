from .models import Psicologia
from rest_framework import serializers

class PsicoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Psicologia
		fields = ('__all__')
