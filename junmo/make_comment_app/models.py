from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField, DateField

class Comment(models.Model):

    c_id = models.IntegerField(primary_key = True, max_length=255,null=False)
    b_id = models.IntegerField(max_length=100)
    t_num = models.IntegerField(max_length=255, null=False)
    u_id = models.CharField(max_length=255, null=False)
    comment = models.CharField(max_length=255, null=False)



    class Meta:
        db_table = 'COMMENT'
        managed = False

# Create your models here.
