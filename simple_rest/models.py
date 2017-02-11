from __future__ import unicode_literals

from django.db import models

class SimpleAPI(models.Model):
	post_title = models.CharField(max_length=25)
	first_name = models.CharField(max_length=25)

	def __self__(self):
		return self.post_title
