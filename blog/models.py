from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

	class Status(models.TextChoices):
		DRAFT='DF', 'Draft'
		PUBLISHED='PB', 'Published'

	title = models.CharField(max_length=200)
	slug = models.SlugField()
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

	class Meta:
		ordering = ['-publish'] # order in descending order

	def __str__(self):
		return self.title