from django.db import models


class Article(models.Model):

	titre = models.CharField(max_length=400) #char dans la db
	image = models.ImageField()
	description = models.TextField()
	prix = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.titre

