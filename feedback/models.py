from django.db import models

# Create your models here.
from account.models import User


class Question(models.Model):
    visitorAccount = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)


class Answer(models.Model):
    visitorAccount = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)