from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)