from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField, DateField
from pandas import to_datetime
# Create your models here.
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
    LEAGUE = models.ForeignKey(LEAGUE, db_column='l_name', on_delete=models.CASCADE, null=True)
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
    CLUB = models.ForeignKey(CLUB, db_column='c_name', on_delete=models.CASCADE, null=True)
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
    #CLUB_ht = models.ForeignKey(CLUB, db_column='c_name', on_delete=models.CASCADE, null=True)
    #hometeam
    # CLUB_at = models.ForeignKey(CLUB, db_column='c_name', on_delete=models.CASCADE, null=True)
    
    date = models.DateTimeField(null= False)
    home_goal = models.IntegerField(max_length=3, null=False)
    away_goal = models.IntegerField(max_length=3, null=False)
    LEAGUE = models.ForeignKey(LEAGUE, db_column ='l_name', on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = 'GAME'
        managed = False    