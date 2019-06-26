from django.db import models

class Meme(models.Model):
	button_id = models.CharField(max_length=200)
	unixtime = models.CharField(max_length=200)
	uuid = models.CharField(max_length=200)
	text = models.CharField(max_length=200)
	s3_url = models.URLField(
						      max_length=128, 
						      db_index=True, 
						      unique=True, 
						      blank=True
						    )
	orig_url = models.URLField(
						      max_length=128, 
						      db_index=True, 
						      unique=True, 
						      blank=True
						    )