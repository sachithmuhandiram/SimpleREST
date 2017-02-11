from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import SimpleAPI
from .serializing_class import SimpleAPISerializer

class SimpleAPIView(APIView):

	def get(self,request):
		posts = SimpleAPI.objects.all()
		serialize_post = SimpleAPISerializer(posts,many=True) # we need to send more records
		return Response(serialize_post.data)

