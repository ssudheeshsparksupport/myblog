from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=90)
	author = models.ForeignKey(User)
	photo=models.ImageField(upload_to='pic_folder')
	content = models.TextField()
	public = models.BooleanField(default=False)
	created = models.DateTimeField(default=datetime.now)  
	updated = models.DateTimeField(null=True, blank=True) 
	published = models.DateTimeField(null=True, blank=True) 
	