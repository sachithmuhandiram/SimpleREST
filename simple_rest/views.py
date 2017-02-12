from django.shortcuts import get_object_or_404	
from rest_framework.views import APIView	# API view
from rest_framework.response import Response
from rest_framework import status

from .models import SimpleAPI 							#our model (database)
from .serializing_class import SimpleAPISerializer		#serializer, which is used tomake data into JSON format

class SimpleAPIView(APIView):				# class view

	def get(self,request):										# only getting method is set
		posts = SimpleAPI.objects.all()							# get all the objects in the modesl
		serialize_post = SimpleAPISerializer(posts,many=True) 	# many=True, because we need to send more records
		return Response(serialize_post.data)		# returning serialized data

