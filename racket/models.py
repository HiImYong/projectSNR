from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.db.models import Avg

from account.models import User


class RacketBrand(models.Model):
    name = models.CharField(max_length=20)

class Racket(models.Model):
    name = models.CharField('라켓이름', max_length=100)
    weight = models.IntegerField('라켓무게', default=0)
    pattern = models.CharField('라켓스트링패턴', max_length=100)
    headsize = models.IntegerField('라켓헤드사이즈', default=0)
    length = models.FloatField('라켓길이', default=0)
    balance = models.CharField('라켓밸런스', max_length=20, default=0)
    # regDateInt = models.IntegerField('라켓생산년도', default=0)
    brand = models.ForeignKey(RacketBrand, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='like')
    visitorAvgScore = models.FloatField('사용자평점평균', default=0)
    countLike = models.IntegerField('좋아요개수', default=0)

    # def countLikeSave(self):
    #     getCount = Racket.values('created', 'name').annotate(product_cnt=Count('name'))
    #
    # self.visitorreview_set.aggregate(Avg('visitorScore'))['visitorScore__avg']

    # def thumb_img_url(self):
    #     img_names = {
    #
    #
    #     }
    #
    #     img_name = img_names[self.name]
    #
    #     return f"https://raw.githubusercontent.com/HiImYong/snrPictures/master/{img_name}.jpg"




class RacketDetail(models.Model):
    racket = models.OneToOneField(Racket, related_name='detail', on_delete=models.CASCADE)
    adminReview = models.TextField()
    adminPower = models.FloatField('운영자파워평점', default=0)
    adminSpin = models.FloatField('운영자스핀평점', default=0)
    adminManeuverability = models.FloatField('운영자조작성평점', default=0)
    adminStability = models.FloatField('운영자면안정성평점', default=0)
    adminComfort = models.FloatField('운영자안락함평점', default=0)
    adminAvgScore = models.FloatField('운영자평점평균', default=0)




