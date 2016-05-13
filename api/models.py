from django.db import models

# Create your models here.

class Colors(models.Model):
	name = models.CharField(max_length=40,blank=False,unique=True)
	hexadecimal = models.CharField(max_length=7,unique=True)
	red = models.PositiveSmallIntegerField(null=True)
	green = models.PositiveSmallIntegerField(null=True)
	blue = models.PositiveSmallIntegerField(null=True)

	def __str__(self):
		return self.name