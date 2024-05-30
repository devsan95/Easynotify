from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Userr(models.Model):

	Name = models.CharField(max_length=255)
	Team = models.ForeignKey(User, on_delete=models.CASCADE)
    
	def __str__(self) -> str:
		return self.title
