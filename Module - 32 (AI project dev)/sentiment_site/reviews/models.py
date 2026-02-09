from django.db import models

# Create your models here.
class Review(models.Model):
    text = models.TextField()
    sentiment_level = models.CharField(max_length=20, blank=True, null=True)
    sentiment_score = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
