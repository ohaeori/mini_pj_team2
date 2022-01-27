from stat import UF_HIDDEN
from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField, DateField

class User(models.Model):
    u_id = models.CharField(primary_key=True, max_length=20, null=False)
    pw = models.CharField(max_length=20, null=False)
    u_name = models.CharField(max_length=20, null=False)
    birth_date = DateField(null=False)
    nickname = models.CharField(max_length=20, null=False)
    phone_num = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)
    class Meta:
        db_table = 'USER'
        app_label = 'member'
        managed = False
