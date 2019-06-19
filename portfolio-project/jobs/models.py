from django.db import models

class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)
	gitLink = models.URLField(
						      max_length=128, 
						      db_index=True, 
						      unique=True, 
						      blank=True
						    )

