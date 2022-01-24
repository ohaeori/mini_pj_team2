from django.db import models
from sympy import content

# Create your models here.

class Notice(models.Model):
    title=models.CharField(max_length=30)
    contents = models.TextField()

    def __str__(self):return self.title