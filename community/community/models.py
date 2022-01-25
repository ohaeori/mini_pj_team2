from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField, DateField
from pandas import to_datetime
# Create your models here.

class USER(models.Model):

    u_id = models.CharField(primary_key=True,  max_length=20, null=False)
    pw = models.CharField(max_length=20, null=False)
    u_name = models.CharField(max_length=20, null=False)
    birth_date = DateField(null=False, default=to_datetime)
    nickname = models.CharField(max_length=20, null=False)
    phone_num = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'USER'
        managed = False

class BOARD(models.Model):
    b_id = models.IntegerField(primary_key=True, max_length=100, null=False)
    b_name = models.CharField(max_length=255,null=False)
    
    class Meta:
        db_table = 'BOARD'
        managed = False


class BOARD_TITLE(models.Model):
    t_num = models.AutoField(primary_key = True,null=False)
    title = models.CharField(max_length=20,null=False)
    date = models.DateTimeField(null=True, auto_now=True)
    content = models.TextField(null=False)
    good = models.IntegerField(null=True)
    url = models.FileField(upload_to='%Y/%m/%d',null=True)

    user = models.ForeignKey(USER, db_column='u_id', on_delete=models.SET_NULL, null=True)
    #u_id = models.CharField(max_length=20,null=True)
    board = models.ForeignKey(BOARD,  db_column='b_id',on_delete=models.SET_NULL, null=True)
    #b_id = models.IntegerField(null=False)
    class Meta:
        db_table = 'BOARD_TITLE'
        managed = False

class COMMENT(models.Model):

    c_id = models.AutoField(primary_key=True, null=False)
    b_id = models.IntegerField(null=False)
    # t_num =models.IntegerField(null=False)
    # u_id = models.CharField(max_length=20, null=False)
    comment = models.CharField(max_length=50, null=False)

    u_id_col = models.ForeignKey(USER, db_column='u_id', on_delete=models.SET_NULL, null=True)
    board_title = models.ForeignKey(BOARD_TITLE, db_column='t_num', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'COMMENT'
        managed = False