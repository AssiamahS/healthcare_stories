from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Duplicate(models.Model):
    original = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='duplicates')
    duplicate = models.ForeignKey(Story, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True)
