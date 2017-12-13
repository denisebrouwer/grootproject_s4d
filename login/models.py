from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	favfood = models.CharField(max_length=100, default='')
	hatefood = models.CharField(max_length=100, default='')
	woonplaats = models.CharField(max_length=100, default='')

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		profile  = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User) 
