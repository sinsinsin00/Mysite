import email
from django.db import models

# Create your models here.
class Feed(models.Model):
    content         = models.TextField()    # 댓글내용
    image           = models.TextField()    # 피드 이미지
    email           = models.EmailField(default='')   # 계정 이메일
    

class Like(models.Model):
    feed_id         = models.IntegerField()
    email           = models.EmailField(default='')   # 계정 이메일
    is_like         = models.BooleanField(default=False)
    
    
class Reply(models.Model):
    feed_id         = models.IntegerField()
    email           = models.EmailField(default='')   # 계정 이메일
    reply_content   = models.TextField()    # 댓글내용
    
    
class BookMark(models.Model):
    feed_id         = models.IntegerField()
    email           = models.EmailField(default='')   # 계정 이메일
    is_marked       = models.BooleanField(default=False)