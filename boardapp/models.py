from stat import UF_HIDDEN
from django.db import models
from django.db.models.fields import CharField, IntegerField, DateTimeField, FloatField, DateField

# Create your models here.

# class User(models.Model):
#     u_id = models.CharField(primary_key=True, max_length=20, null=False)
#     pw = models.CharField(max_length=20, null=False)
#     u_name = models.CharField(max_length=20, null=False)
#     birth_date = DateField(null=False)
#     nickname = models.CharField(max_length=20, null=False)
#     phone_num = models.CharField(max_length=20, null=True)
#     e_mail = models.CharField(max_length=50, null=True)
#     class Meta:
#         db_table = 'USER'
#         app_label = 'boardapp'
#         managed = False


# class Board(models.Model):
#     b_id = models.IntegerField(primary_key=True, max_length=100, null=False)
#     b_name = models.CharField(max_length=255,null=False)
    
#     class Meta:
#         db_table = 'BOARD'
#         app_label = 'boardapp'
#         managed = False

class Board_title(models.Model):
    t_num = models.IntegerField(primary_key = True,null=False)
    b_id = models.IntegerField(null=False)
    title = models.CharField(max_length=20,null=False)
    u_id = models.CharField(max_length=20,null=False)
    date = models.DateTimeField(null=False)
    content = models.TextField(null=False)
    good = models.IntegerField(null=True)

    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'BOARD_TITLE'
        app_label = 'boardapp'
        managed = False

class Comment(models.Model):

  c_id = models.IntegerField(primary_key=True, null=False)
  b_id = models.IntegerField(null=False)
  t_num =models.IntegerField(null=False)
  u_id = models.CharField(max_length=20, null=False)
  comment = models.CharField(max_length=50, null=False)

#  board_title = models.ForeignKey(Board_title, on_delete=models.SET_NULL, null=True)
  

  class Meta:
    db_table = 'COMMENT'
    app_label = 'boardapp'
    managed = False




# class Good(models.Model):
#     u_id = models.CharField(max_length=20, null=False)
#     t_num =models.IntegerField(null=False)
#     class Meta:
#         unique_together = (('u_id', 't_num'),)
#         db_table = 'GOOD'
#         app_label = 'boardapp'
#         managed = False

                  