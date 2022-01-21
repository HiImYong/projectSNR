from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
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

    def thumb_img_url(self):

        img_names = {
            1: '블레이드 98 덴스',
            2: '퓨어 드라이브',
            3: '퓨어 에어로',
            4: '스피드 프로',
            5: '프레스티지 프로',
            6: '그래비티 투어',
            7: '프로스태프 97 RF',
            8: '라디칼 프로'
        }

        img_name = img_names[self.id]

        return f"https://raw.githubusercontent.com/HiImYong/snrPictures/master/{img_name}.jpg"




class RacketDetail(models.Model):
    racket = models.ForeignKey(Racket, on_delete=models.CASCADE, default=999999)
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





