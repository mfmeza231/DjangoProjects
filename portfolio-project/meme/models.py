from django.db import models

class Meme(models.Model):
	unixtime = models.CharField(max_length=200)
	s3_url = models.URLField(
						      max_length=128, 
						      db_index=True, 
						      unique=True, 
						      blank=True
						    )