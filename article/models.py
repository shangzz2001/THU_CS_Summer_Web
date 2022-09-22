from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # title = models.CharField(max_length=100)
    # body = models.TextField()
    # created = models.DateTimeField(default=timezone.now)
    # updated = models.DateTimeField(auto_now=True)
    # author = models.CharField(max_length=20)
    pre_id = models.CharField(max_length=20,default="UnKnown")
    title = models.CharField(max_length=100)
    body = models.TextField()
    likes = models.PositiveIntegerField(default=0)  # 原博客的获赞数
    favors = models.PositiveIntegerField(default=0) # 原博客的收藏数
    comments = models.PositiveIntegerField(default=0) # 原博客的评论数
    views = models.PositiveBigIntegerField(default=0) # 原博客的浏览量
    create_time = models.CharField(max_length=20)  # 原本博客创建的时间
    # created = models.DateTimeField(default=timezone.now)
    passage_url = models.CharField(max_length=50)  # 博客的原文链接
    tag = models.CharField(max_length=10,default='else')
    abs = models.CharField(max_length=50,default='Empty') #原博客的摘要
    author_url = models.CharField(max_length=50,default='Empty') #原文作者主页
    author_img_src = models.CharField(max_length=50,default='/media/user_img/default.png') # 原文作者头像
    author_followers = models.PositiveBigIntegerField(default=0) # 作者粉丝
    author_articles = models.PositiveBigIntegerField(default=0) #作者文章数
    author_likes = models.PositiveBigIntegerField(default=0) # 作者关注数
    class Meta:
        ordering = ('-create_time',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])
    
    
