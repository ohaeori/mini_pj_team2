from django.db import models
from django.db.models.fields import CharField, IntegerField, DateTimeField, FloatField, DateField
# Create your models here.
from pandas import to_datetime

class LEAGUE(models.Model):
    l_name = models.CharField(primary_key=True, max_length=50, null=False)
    l_coun = models.CharField(max_length=50, null=False)
    team_count = models.IntegerField(max_length=10,null=False)
    image = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = 'LEAGUE'
        managed = False    




class CLUB(models.Model):
    c_name =models.CharField(primary_key=True, max_length=50, null=False)
    #l_name = models.CharField(max_length=50, null=False) # 관계설정해주기
    league = models.ForeignKey(LEAGUE, db_column='l_name', on_delete=models.CASCADE, null=True)
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


class PLAYER(models.Model):
    p_id = models.IntegerField(primary_key=True,max_length=10, null=False)
    p_name = models.CharField(max_length=50, null=False)
    back_num = models.IntegerField(max_length=11, null=False)
    height = models.IntegerField(max_length=11, null=False)
    weight = models.IntegerField(max_length=11, null=False)
    birth_date = DateField(null=False)
    # c_name = models.CharField(max_length=50, null=False)
    club = models.ForeignKey(CLUB, db_column='c_name', on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=10, null=False)
    image =models.CharField(max_length=1000, null=False)
    country = models.CharField(max_length=20, null=False)
    
    class Meta:
        db_table = 'PLAYER'
        managed = False    


class GAME(models.Model):
    g_id = models.AutoField(primary_key=True, null=False)
    home_team = models.CharField(max_length=50, null=False)
    away_team = models.CharField(max_length=50, null=False)
    #CLUB_ht = models.ForeignKey(CLUB, db_column='home_team', on_delete=models.CASCADE, null=True)
    #hometeam
    # CLUB_at = models.ForeignKey(CLUB, db_column='c_name', on_delete=models.CASCADE, null=True)
    
    date = models.DateTimeField(null= False)
    home_goal = models.IntegerField(max_length=3, null=False)
    away_goal = models.IntegerField(max_length=3, null=False)
    LEAGUE = models.ForeignKey(LEAGUE, db_column ='l_name', on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = 'GAME'
        managed = False    


class NEWS(models.Model):
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