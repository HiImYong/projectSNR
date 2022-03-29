

from django.db import models
from django.contrib.auth import get_user_model as user_model
User = user_model()

# Create your models here.


class Article(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    regDate = models.DateTimeField(auto_now_add=True)
    visitorAccount = models.ForeignKey(User, on_delete=models.CASCADE)


class Reply(models.Model):
    articleForeignKey = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    regDate = models.DateTimeField(auto_now_add=True)
    visitorAccount = models.ForeignKey(User, on_delete=models.CASCADE)

