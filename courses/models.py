from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.urls import reverse


from PIL import Image

DURATION_CHOICES = [
	(2, '2 Weeks'),
	(8, '8 Weeks'),
]

class Course(models.Model):
	title = models.CharField(max_length = 50, default ="Name it something good")
	description = models.TextField()
	instructor = models.CharField(max_length = 50, default = "Django Guru")
	duration = models.IntegerField(choices=DURATION_CHOICES, default = 8)
	art = models.ImageField(upload_to='courseart/')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('courses:detail', kwargs={'pk': self.pk})
