from rest_framework import serializers
from cognotest import models

class CognoSerializer(serializers.ModelSerializer):
	"""docstring for CognoSerializer"""
	class Meta:
		fields = (
			'id',
			'name',
			)
		model = models.Cogno
		