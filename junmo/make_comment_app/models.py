from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField, DateField
from pandas import to_datetime

class User(models.Model):

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

class Board_title(models.Model):
    t_num = models.AutoField(primary_key = True,null=False)
    b_id = models.IntegerField(null=False)
    title = models.CharField(max_length=20,null=False)
    u_id = models.CharField(max_length=20,null=False)
    date = models.DateTimeField(null=False)
    content = models.TextField(null=False)
    good = models.IntegerField(null=True)
    image = models.ImageField(blank=True, null=True)
    url = models.FileField(upload_to='%Y/%m/%d',null=True)

    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'BOARD_TITLE'
        managed = False

class Comment(models.Model):

    c_id = models.AutoField(primary_key=True, null=False)
    b_id = models.IntegerField(null=False)
    # t_num =models.IntegerField(null=False)
    # u_id = models.CharField(max_length=20, null=False)
    comment = models.CharField(max_length=50, null=False)

    u_id_col = models.ForeignKey(User, db_column='u_id', on_delete=models.SET_NULL, null=True)
    board_title = models.ForeignKey(Board_title, db_column='t_num', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'COMMENT'
        managed = False