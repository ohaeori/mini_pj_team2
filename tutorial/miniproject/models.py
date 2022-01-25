from tarfile import DEFAULT_FORMAT
from django.db import models

# Create your models here.
class League(models.Model):
    l_name = models.CharField(primary_key = True,max_length=255, null=False)
    l_con = models.CharField(max_length=255, null=True)
    l_data = models.IntegerField(null=True)
    
    class Meta:
        db_table = 'LEAGUE'
        managed = False

class Player(models.Model):
    name = models.CharField(primary_key = True,max_length=255,null=False)

    class Meta:
        db_table = 'PLAYER'
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

    class Meta:
        db_table = 'BOARD_TITLE'
        managed = False

class Comment(models.Model):
  c_id = models.AutoField(primary_key=True, null=False)
  b_id = models.IntegerField(null=False)
  u_id = models.CharField(max_length=20, null=False)
  comment = models.CharField(max_length=50, null=False)
  board_title = models.ForeignKey(Board_title, db_column='t_num', on_delete=models.SET_NULL, null=True)

  class Meta:
    db_table = 'COMMENT'
    managed = False
    

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
    news = models.ForeignKey(News, db_column='n_id', on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(null=False)
    u_id = models.CharField(max_length=20, default='이름없음')

    class Meta:
        db_table = 'NEWS_COMMENT'
        managed = False


