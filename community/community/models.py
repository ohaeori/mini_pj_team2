from django.db import models

# Create your models here.

class BOARD_TITLE(models.Model):
    t_num = models.AutoField(primary_key = True,null=False)
    b_id = models.IntegerField(null=False)
    title = models.CharField(max_length=20,null=False)
    u_id = models.CharField(max_length=20,null=True)
    date = models.DateTimeField(null=True, auto_now=True)
    content = models.TextField(null=False)
    good = models.IntegerField(null=True)
    url = models.FileField(upload_to='%Y/%m/%d',null=True)
    class Meta:
        db_table = 'BOARD_TITLE'
        managed = False