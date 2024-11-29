from django.db import models

# Create your models here.

class RacePost(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    elevation = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    