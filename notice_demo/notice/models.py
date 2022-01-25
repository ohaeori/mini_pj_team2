from django.db import models
from isort import file
from sympy import content

# Create your models here.

class Notice(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d',null=True)
    title=models.CharField(max_length=30)
    contents = models.TextField()
    photo=models.ImageField(blank=True, null=True)
    
    def __str__(self):return self.title


class UploadFile(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d')
