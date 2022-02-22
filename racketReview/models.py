from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from racket.models import Racket

from django.contrib.auth import get_user_model as user_model

User = user_model()


# Create your models here.

class RacketReviewModel(models.Model):
    visitorAccount = models.ForeignKey(User, on_delete=models.CASCADE)
    visitorReview = models.TextField()
    visitorRacket = models.ForeignKey(Racket, on_delete=models.CASCADE)
    visitorScore = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)



