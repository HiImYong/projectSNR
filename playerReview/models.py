from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from player.models import Player

from django.contrib.auth import get_user_model as user_model
User = user_model()


# Create your models here.

class PlayerReviewModel(models.Model):
    visitorAccount = models.ForeignKey(User, on_delete=models.CASCADE)
    visitorReview = models.TextField()
    visitorPlayer = models.ForeignKey(Player, on_delete=models.CASCADE)
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
