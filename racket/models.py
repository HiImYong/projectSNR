from django.db import models

# Create your models here.
class Racket(models.Model):
    name = models.CharField('라켓이름', max_length=20)
    weight = models.IntegerField('라켓무게', default=0)
    pattern = models.CharField('라켓스트링패턴', max_length=20)
    headsize = models.IntegerField('라켓헤드사이즈', default=0)
    length = models.FloatField('라켓길이', default=0)
    balance = models.IntegerField('라켓밸런스', default=0)
    hitCount = models.PositiveIntegerField('조회수', default=0)

