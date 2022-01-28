from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.db.models import Avg

from account.models import User


class Racket(models.Model):
    name = models.CharField('라켓이름', max_length=20)
    weight = models.IntegerField('라켓무게', default=0)
    pattern = models.CharField('라켓스트링패턴', max_length=20)
    headsize = models.IntegerField('라켓헤드사이즈', default=0)
    length = models.FloatField('라켓길이', default=0)
    balance = models.IntegerField('라켓밸런스', default=0)
    regDateInt = models.IntegerField('라켓생산년도', default=0)
    hitCount = models.PositiveIntegerField('조회수', default=0)
    manufacturer = models.CharField('제조사', max_length=20, default="등록전")
    like = models.ManyToManyField(User, related_name='like')

    @property
    def visitorReviewScore(self):
        return self.visitorreview_set.aggregate(Avg('visitorScore'))['visitorScore__avg']


    def thumb_img_url(self):
        img_names = {
            1: '블레이드 98 덴스',
            2: '퓨어 드라이브',
            3: '퓨어 에어로',
            4: '스피드 프로',
            5: '프레스티지 프로',
            6: '그래비티 투어',
            7: '프로스태프 97 RF v5',
            8: '라디칼 프로',
            9: '퓨어스트라이크 98 오픈 v3',
            10: '퓨어스트라이크 98 덴스 v3',
            11: '프로스태프 97 RF v1',
            12: '요넥스 브이코어 프로 HG v2',
            13: '요넥스 브이코어 프로 HG v1',
            14: '요넥스 브이코어 프로 v1',
            15: '요넥스 브이코어 프로 v2',
            16: '브이필 8 300g',
            17: '퓨어 에어로 라파',
            18: '프로스태프 97S v1',
            19: '퓨어 드라이브 v3',
            20: '퓨어 드라이브 v4',
            21: '퓨어 드라이브 v5',
            22: '퓨어 드라이브 v6',
            23: '퓨어 드라이브 v7',
            24: '퓨어 드라이브 v8',
            25: '퓨어 드라이브 v4',
            26: '퓨어 드라이브 v4 로딕',
            27: '퓨어 드라이브 v4 로딕 플러스',
            28: '퓨어 드라이브 v5 로딕',
            29: '퓨어 드라이브 v5 로딕 플러스',
            30: '퓨어 드라이브 v6 로딕',
            31: '퓨어 드라이브 v7 투어',
            32: '퓨어 드라이브 v8 투어',
            33: '브이코어 95 v1',
            34: '브이코어 95 v2',
            35: '프로스태프 97 RF v2',
            36: '프로스태프 97 RF v3',
            37: '스피드 프로 v1',
            38: '스피드 프로 v2',
            39: '스피드 프로 v3',
            40: '스피드 프로 v4',
            41: '스피드 프로 v5',
            42: '스피드 프로 v6',
            43: '스피드 프로 v7',
            44: '큐5 315',

        }

        img_name = img_names[self.id]

        return f"https://raw.githubusercontent.com/HiImYong/snrPictures/master/{img_name}.jpg"


class RacketDetail(models.Model):
    racket = models.OneToOneField(Racket, related_name='detail', on_delete=models.CASCADE)
    adminReview = models.TextField()
    adminPower = models.FloatField('운영자파워평점', default=0)
    adminSpin = models.FloatField('운영자스핀평점', default=0)
    adminManeuverability = models.FloatField('운영자조작성평점', default=0)
    adminStability = models.FloatField('운영자면안정성평점', default=0)
    adminComfort = models.FloatField('운영자안락함평점', default=0)

    @property
    def adminAvgScore(self):
        scoreAvg = (
                           self.adminPower +
                           self.adminSpin +
                           self.adminManeuverability +
                           self.adminStability +
                           self.adminComfort
                   ) / 5
        return round(scoreAvg, 2)
