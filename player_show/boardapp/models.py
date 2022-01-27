from stat import UF_HIDDEN
from turtle import back
from django.db import models
from django.db.models.fields import CharField, IntegerField, DateTimeField, FloatField, DateField
from sqlalchemy import null

# Create your models here.

class User(models.Model):
    u_id = models.CharField(primary_key=True, max_length=20, null=False)
    pw = models.CharField(max_length=20, null=False)
    u_name = models.CharField(max_length=20, null=False)
    birth_date = DateField(null=False)
    nickname = models.CharField(max_length=20, null=False)
    phone_num = models.CharField(max_length=20, null=True)
    e_mail = models.CharField(max_length=50, null=True)
    class Meta:
        db_table = 'USER'
        app_label = 'boardapp'
        managed = False


class Board(models.Model):
    b_id = models.IntegerField(primary_key=True, max_length=100, null=False)
    b_name = models.CharField(max_length=255,null=False)
    
    class Meta:
        db_table = 'BOARD'
        app_label = 'boardapp'
        managed = False

class Board_title(models.Model):
    t_num = models.AutoField(primary_key = True,null=False)
    #b_id = models.IntegerField(null=False)
    title = models.CharField(max_length=20,null=False)
    #u_id = models.CharField(max_length=20,null=False)
    date = models.DateTimeField(null=False)
    content = models.TextField(null=False)
    good = models.IntegerField(null=True)
    url = models.FileField(upload_to='%Y/%m/%d',null=True)
    image = models.ImageField(blank=True, null=True)

    user = models.ForeignKey(User, db_column='u_id', on_delete=models.SET_NULL, null=True)
    board = models.ForeignKey(Board,  db_column='b_id',on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'BOARD_TITLE'
        app_label = 'boardapp'
        managed = False

class Comment(models.Model):

  c_id = models.AutoField(primary_key=True, null=False)
  b_id = models.IntegerField(null=False)
  # t_num = models.IntegerField(null=False)
  u_id = models.CharField(max_length=20, null=False)
  comment = models.CharField(max_length=50, null=False)

  board_title = models.ForeignKey(Board_title, db_column='t_num', on_delete=models.SET_NULL, null=True)
  

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


class News(models.Model):
    n_id = models.AutoField(primary_key=True, max_length = 255)
    n_title = models.CharField(max_length = 200,null=False)
    content = models.TextField(null=False)
    date = models.DateTimeField(null=False)
    image = models.ImageField(blank=True, null=True)
    press = models.CharField(max_length=20,null=False)
    league = models.CharField(max_length=20,null=True)

    class Meta:
        db_table = 'NEWS'
        managed = False


class News_Comment(models.Model):
    c_id = models.AutoField(primary_key=True, null=False)
    comment = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(null=False)
    u_id = models.CharField(max_length=20, default='이름없음')
    
    news = models.ForeignKey(News, db_column='n_id', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'NEWS_COMMENT'
        managed = False                

######################################################
class League(models.Model):
    l_name = models.CharField(primary_key=True, max_length=50, null=False)
    l_coun = models.CharField(max_length=50, null=False)
    team_count = models.IntegerField(max_length=10,null=False)
    image = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = 'LEAGUE'
        managed = False    




class Club(models.Model):
    c_name =models.CharField(primary_key=True, max_length=50, null=False)
    #l_name = models.CharField(max_length=50, null=False) # 관계설정해주기
    league = models.ForeignKey(League, db_column='l_name', on_delete=models.CASCADE, null=True)
    stadium = models.CharField(max_length=50, null=False)
    rank = models.IntegerField(max_length=10, null=False)
    played = models.IntegerField(max_length=10, null=False)
    pts = models.IntegerField(max_length=10, null=False)
    w = models.IntegerField(max_length=10, null=False)
    d = models.IntegerField(max_length=10, null=False)
    l = models.IntegerField(max_length=10, null=False)
    gf = models.IntegerField(max_length=10, null=False)
    ga = models.IntegerField(max_length=10, null=False)
    gd = models.IntegerField(max_length=10, null=False)
    image = models.CharField(max_length=1000, null=False)
    class Meta:
        db_table = 'CLUB'
        managed = False                


class Player(models.Model):
    p_id = models.IntegerField(primary_key=True,max_length=10, null=False)
    p_name = models.CharField(max_length=50, null=False)
    back_num = models.IntegerField(max_length=11, null=False)
    height = models.IntegerField(max_length=11, null=False)
    weight = models.IntegerField(max_length=11, null=False)
    birth_date = DateField(null=False)
    # c_name = models.CharField(max_length=50, null=False)
    club = models.ForeignKey(Club, db_column='c_name', on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=10, null=False)
    image =models.CharField(max_length=1000, null=False)
    country = models.CharField(max_length=20, null=False)
    
    class Meta:
        db_table = 'PLAYER'
        managed = False    


class Game(models.Model):
    g_id = models.AutoField(primary_key=True, null=False)
    #home_team = models.CharField(max_length=50, null=False)
    away_team = models.CharField(max_length=50, null=False)
    club_ht = models.ForeignKey(Club, db_column='c_name', on_delete=models.CASCADE, null=True)
    # club_at = models.ForeignKey(Club, db_column='c_name', on_delete=models.CASCADE, null=True)
    
    date = models.DateTimeField(null= False)
    home_goal = models.IntegerField(max_length=3, null=False)
    away_goal = models.IntegerField(max_length=3, null=False)
    league = models.ForeignKey(League, db_column ='l_name', on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = 'GAME'
        managed = False    