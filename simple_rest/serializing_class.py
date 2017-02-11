from rest_framework import serializers
from .models import SimpleAPI

class SimpleAPISerializer(serializers.ModelSerializer):

	class Meta:
		model = SimpleAPI
		#fields = ('post_title','first_name')
		fields = '__all__'