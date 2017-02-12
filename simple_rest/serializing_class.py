from rest_framework import serializers
from .models import SimpleAPI

class SimpleAPISerializer(serializers.ModelSerializer):

	class Meta:
		model = SimpleAPI 		#our model (database)
		fields = ('post_title','first_name')	# only these two colums return
		#fields = '__all__'						# all the data is returned, including id