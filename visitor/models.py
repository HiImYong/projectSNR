from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from racket.models import Racket

from django.contrib.auth import get_user_model as user_model

User = user_model()


# Create your models here.

class VisitorReview(models.Model):
    visitorAccount = models.ForeignKey(User, on_delete=models.CASCADE)
    visitorReview = models.CharField('라켓 리뷰', max_length=500)
    visitorRacket = models.ForeignKey(Racket, on_delete=models.CASCADE)
    visitorScore = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])



