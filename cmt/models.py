from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from article.models import ArticlePost

# 博文的评论
class Cmt(models.Model):
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='cmt'
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]