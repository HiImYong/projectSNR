from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.db.models import Avg

from account.models import User


class RacketBrand(models.Model):
    name = models.CharField('라켓제조사', max_length=20)

class Racket(models.Model):
    name = models.CharField('라켓이름', max_length=30)
    weight = models.IntegerField('라켓무게', default=0)
    pattern = models.CharField('라켓스트링패턴', max_length=20)
    headsize = models.IntegerField('라켓헤드사이즈', default=0)
    length = models.FloatField('라켓길이', default=0)
    balance = models.IntegerField('라켓밸런스', default=0)
    regDateInt = models.IntegerField('라켓생산년도', default=0)
    # manufacturer = models.CharField('제조사', max_length=20, default="등록전")
    brand = models.ForeignKey(RacketBrand, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='like')
    visitorAvgScore = models.FloatField('사용자평점평균', default=0)
    countLike = models.IntegerField('좋아요개수', default=0)

    # def countLikeSave(self):
    #     getCount = Racket.values('created', 'name').annotate(product_cnt=Count('name'))
    #
    # self.visitorreview_set.aggregate(Avg('visitorScore'))['visitorScore__avg']

    def thumb_img_url(self):
        img_names = {
            '퓨어 드라이브 v9': '퓨어 드라이브 v9',
            '퓨어 에어로 v2': '퓨어 에어로 v2',
            '그래비티 프로 v1': '그래비티 프로 v1',
            '프로스태프 97 RF v4': '프로스태프 97 RF v4',
            '퓨어스트라이크 98 오픈 v3': '퓨어스트라이크 98 오픈 v3',
            '퓨어스트라이크 98 덴스 v3': '퓨어스트라이크 98 덴스 v3',
            '프로스태프 97 RF v1': '프로스태프 97 RF v1',
            '브이코어 프로 HG v2': '브이코어 프로 HG v2',
            '브이코어 프로 HG v1': '브이코어 프로 HG v1',
            '브이코어 프로 v1': '브이코어 프로 v1',
            '브이코어 프로 v2': '브이코어 프로 v2',
            '브이필 8 300g': '브이필 8 300g',
            '프로스태프 97S v1': '프로스태프 97S v1',
            '퓨어 드라이브 v3': '퓨어 드라이브 v3',
            '퓨어 드라이브 v4': '퓨어 드라이브 v4',
            '퓨어 드라이브 v5': '퓨어 드라이브 v5',
            '퓨어 드라이브 v6': '퓨어 드라이브 v6',
            '퓨어 드라이브 v7': '퓨어 드라이브 v7',
            '퓨어 드라이브 v8': '퓨어 드라이브 v8',
            '퓨어 드라이브 v4 로딕': '퓨어 드라이브 v4 로딕',
            '퓨어 드라이브 v4 로딕 플러스': '퓨어 드라이브 v4 로딕 플러스',
            '퓨어 드라이브 v5 로딕': '퓨어 드라이브 v5 로딕',
            '퓨어 드라이브 v5 로딕 플러스': '퓨어 드라이브 v5 로딕 플러스',
            '퓨어 드라이브 v6 로딕': '퓨어 드라이브 v6 로딕',
            '퓨어 드라이브 v7 투어': '퓨어 드라이브 v7 투어',
            '퓨어 드라이브 v8 투어': '퓨어 드라이브 v8 투어',
            '브이코어 95 v1': '브이코어 95 v1',
            '브이코어 95 v2': '브이코어 95 v2',
            '프로스태프 97 RF v2': '프로스태프 97 RF v2',
            '프로스태프 97 RF v3': '프로스태프 97 RF v3',
            '스피드 프로 v1 유텍': '스피드 프로 v1 유텍',
            '스피드 프로 v2 유텍 IG': '스피드 프로 v2 유텍 IG',
            '스피드 프로 v3 그라핀': '스피드 프로 v3 그라핀',
            '스피드 프로 v4 그라핀 XT': '스피드 프로 v4 그라핀 XT',
            '스피드 프로 v5 그라핀 터치': '스피드 프로 v5 그라핀 터치',
            '스피드 프로 v6 그라핀 360': '스피드 프로 v6 그라핀 360',
            '스피드 프로 v7 그라핀 360 플러스': '스피드 프로 v7 그라핀 360 플러스',
            '큐5 315': '큐5 315',
            '익스트림 투어 v1 그라핀 360 플러스': '익스트림 투어 v1 그라핀 360 플러스',
            '퓨어 에어로 VS v1': '퓨어 에어로 VS v1',
            '퓨어 에어로 VS v2': '퓨어 에어로 VS v2',
            '에어로 드라이브 v1': '에어로 드라이브 v1',
            '에어로 드라이브 v2': '에어로 드라이브 v2',
            '에어로 드라이브 v3': '에어로 드라이브 v3',
            '에어로 드라이브 v4': '에어로 드라이브 v4',
            '에어로 스톰 v1': '에어로 스톰 v1',
            '퓨어 에어로 v1': '퓨어 에어로 v1',
            '헤리티지 100': '헤리티지 100',
            '식스원 투어 90 - 엔코드': '식스원 투어 90 - 엔코드',
            '식스원 투어 90 - 엔코드(한정판)': '식스원 투어 90 - 엔코드(한정판)',
            '식스원 투어 90 - 케이펙터': '식스원 투어 90 - 케이펙터',
            '식스원 투어 90 - 케이펙터(아시아)': '식스원 투어 90 - 케이펙터(아시아)',
            '식스원 투어 90 - BLX': '식스원 투어 90 - BLX',
            '식스원 투어 90 - BLX(아시아)': '식스원 투어 90 - BLX(아시아)',
            '식스원 투어 90 - BLX 프로스태프 v1': '식스원 투어 90 - BLX 프로스태프 v1',
            '식스원 투어 90 - BLX 프로스태프 v2': '식스원 투어 90 - BLX 프로스태프 v2',
            '번 95 v1': '번 95 v1',
            '번 95 v2': '번 95 v2',
            '주스 프로': '주스 프로',
            '퓨어 드라이브 v6 107': '퓨어 드라이브 v6 107',
            '퓨어 드라이브 v7 107': '퓨어 드라이브 v7 107',
            '퓨어 드라이브 v8 107': '퓨어 드라이브 v8 107',
            '퓨어 드라이브 v9 107': '퓨어 드라이브 v9 107',
            '프로스태프 88 케이팩터': '프로스태프 88 케이팩터',
            '프로스태프 6.0 85': '프로스태프 6.0 85',
            '프로스태프 6.0 95': '프로스태프 6.0 95',
            '브이코어 100 v1': '브이코어 100 v1',
            'CX 200 투어 v1 (덴스)': 'CX 200 투어 v1 (덴스)',
            'CX 200 투어 v2 (덴스)': 'CX 200 투어 v2 (덴스)',
            'CX 200 투어 v1 (오픈)': 'CX 200 투어 v1 (오픈)',
            'CX 200 투어 v2 (오픈)': 'CX 200 투어 v2 (오픈)',
            '울트라 100 v2': '울트라 100 v2',
            '울트라 100 v3': '울트라 100 v3',
            '울트라 97 v1': '울트라 97 v1',
            '울트라 97 v2': '울트라 97 v2',
            '울트라 97 v3': '울트라 97 v3',
            '블레이드 98 엔코드': '블레이드 98 엔코드',
            '블레이드 98 케이펙터': '블레이드 98 케이펙터',
            '블레이드 98 BLX (덴스)': '블레이드 98 BLX (덴스)',
            '블레이드 98 BLX v2 (덴스)': '블레이드 98 BLX v2 (덴스)',
            '블레이드 98 v5 (덴스)': '블레이드 98 v5 (덴스)',
            '블레이드 98 v6 (덴스)': '블레이드 98 v6 (덴스)',
            '블레이드 98 v7 (덴스)': '블레이드 98 v7 (덴스)',
            '블레이드 98 v8 (덴스)': '블레이드 98 v8 (덴스)',
            '블레이드 98 BLX (오픈)': '블레이드 98 BLX (오픈)',
            '블레이드 98 BLX v2 (오픈)': '블레이드 98 BLX v2 (오픈)',
            '블레이드 98 v5 (오픈)': '블레이드 98 v5 (오픈)',
            '블레이드 98 v6 (오픈)': '블레이드 98 v6 (오픈)',
            '블레이드 98 v7 (오픈)': '블레이드 98 v7 (오픈)',
            '블레이드 98 v8 (오픈)': '블레이드 98 v8 (오픈)',
            '퓨어스트라이크 98 오픈 v2': '퓨어스트라이크 98 오픈 v2',
            '퓨어스트라이크 98 덴스 v2': '퓨어스트라이크 98 덴스 v2',
            '프레스티지 MP 인텔리전스': '프레스티지 MP 인텔리전스',
            '프레스티지 MP 리퀴드메탈': '프레스티지 MP 리퀴드메탈',
            '프레스티지 MP 플렉스포인트': '프레스티지 MP 플렉스포인트',
            '프레스티지 MP 마이크로젤': '프레스티지 MP 마이크로젤',
            '프레스티지 MP 유텍': '프레스티지 MP 유텍',
            '프레스티지 MP 유텍 IG': '프레스티지 MP 유텍 IG',
            '프레스티지 MP 그라핀': '프레스티지 MP 그라핀',
            '프레스티지 MP 그라핀 XT': '프레스티지 MP 그라핀 XT',
            '프레스티지 MP 그라핀 터치': '프레스티지 MP 그라핀 터치',
            '프레스티지 MP 그라핀 360': '프레스티지 MP 그라핀 360',
            '프레스티지 MP 그라핀 360 플러스': '프레스티지 MP 그라핀 360 플러스',
            '프레스티지 PRO': '프레스티지 PRO',
            '프레스티지 MID 리퀴드메탈': '프레스티지 MID 리퀴드메탈',
            '프레스티지 MID 플렉스포인트': '프레스티지 MID 플렉스포인트',
            '프레스티지 MID 마이크로젤': '프레스티지 MID 마이크로젤',
            '프레스티지 MID 유텍': '프레스티지 MID 유텍',
            '프레스티지 MID 유텍 IG': '프레스티지 MID 유텍 IG',
            '프레스티지 REV PRO 그라핀': '프레스티지 REV PRO 그라핀',
            '프레스티지 REV PRO 그라핀 XT': '프레스티지 REV PRO 그라핀 XT',
            '프레스티지 MID 그라핀 터치': '프레스티지 MID 그라핀 터치',
            '프레스티지 MID 그라핀 360': '프레스티지 MID 그라핀 360',
            '프레스티지 MID 그라핀 360 플러스': '프레스티지 MID 그라핀 360 플러스',
            '프레스티지 PRO 마이크로젤': '프레스티지 PRO 마이크로젤',
            '프레스티지 PRO 유텍': '프레스티지 PRO 유텍',
            '프레스티지 PRO 유텍 IG': '프레스티지 PRO 유텍 IG',
            '프레스티지 PRO 그라핀': '프레스티지 PRO 그라핀',
            '프레스티지 PRO 그라핀 XT': '프레스티지 PRO 그라핀 XT',
            '프레스티지 PRO 그라핀 터치': '프레스티지 PRO 그라핀 터치',
            '프레스티지 PRO 그라핀 360': '프레스티지 PRO 그라핀 360',
            '프레스티지 PRO 그라핀 360 플러스': '프레스티지 PRO 그라핀 360 플러스',
            '라디칼 MP 리퀴드메탈': '라디칼 MP 리퀴드메탈',
            '라디칼 MP 플렉스포인트': '라디칼 MP 플렉스포인트',
            '라디칼 MP 마이크로젤': '라디칼 MP 마이크로젤',
            '라디칼 MP 유텍': '라디칼 MP 유텍',
            '라디칼 MP 유텍 IG': '라디칼 MP 유텍 IG',
            '라디칼 MP 그라핀': '라디칼 MP 그라핀',
            '라디칼 MP 그라핀 XT': '라디칼 MP 그라핀 XT',
            '라디칼 MP 그라핀 터치': '라디칼 MP 그라핀 터치',
            '라디칼 MP 그라핀 360': '라디칼 MP 그라핀 360',
            '라디칼 MP 그라핀 360 플러스': '라디칼 MP 그라핀 360 플러스',
            '라디칼 PRO 유텍': '라디칼 PRO 유텍',
            '라디칼 PRO 유텍 IG': '라디칼 PRO 유텍 IG',
            '라디칼 PRO 그라핀': '라디칼 PRO 그라핀',
            '라디칼 PRO 그라핀 XT': '라디칼 PRO 그라핀 XT',
            '라디칼 PRO 그라핀 터치': '라디칼 PRO 그라핀 터치',
            '라디칼 PRO 그라핀 360': '라디칼 PRO 그라핀 360',
            '라디칼 PRO 그라핀 360 플러스': '라디칼 PRO 그라핀 360 플러스',
            '붐 MP': '붐 MP',
            '붐 프로': '붐 프로',
            '6.1 클래식 (오픈)': '6.1 클래식 (오픈)',
            '6.1 엔코드 (오픈)': '6.1 엔코드 (오픈)',
            '6.1 케이펙터 (오픈)': '6.1 케이펙터 (오픈)',
            '6.1 BLX v1 (오픈)': '6.1 BLX v1 (오픈)',
            '6.1 BLX v2 (오픈)': '6.1 BLX v2 (오픈)',
            '6.1 (오픈)': '6.1 (오픈)',
            '익스트림 MP 마이크로젤': '익스트림 MP 마이크로젤',
            '익스트림 MP 유텍': '익스트림 MP 유텍',
            '익스트림 MP 유텍 IG v1': '익스트림 MP 유텍 IG v1',
            '익스트림 MP 유텍 IG v2': '익스트림 MP 유텍 IG v2',
            '익스트림 MP 그라핀': '익스트림 MP 그라핀',
            '익스트림 MP 그라핀 XT': '익스트림 MP 그라핀 XT',
            '익스트림 MP 그라핀 터치': '익스트림 MP 그라핀 터치',
            '익스트림 MP 그라핀 360': '익스트림 MP 그라핀 360',
            '익스트림 MP 그라핀 360 플러스': '익스트림 MP 그라핀 360 플러스',
            '익스트림 PRO 마이크로젤': '익스트림 PRO 마이크로젤',
            '익스트림 PRO 유텍': '익스트림 PRO 유텍',
            '익스트림 PRO 유텍 IG v1': '익스트림 PRO 유텍 IG v1',
            '익스트림 PRO 유텍 IG v2': '익스트림 PRO 유텍 IG v2',
            '익스트림 PRO 그라핀': '익스트림 PRO 그라핀',
            '익스트림 PRO 그라핀 XT': '익스트림 PRO 그라핀 XT',
            '익스트림 PRO 그라핀 터치': '익스트림 PRO 그라핀 터치',
            '익스트림 PRO 그라핀 360': '익스트림 PRO 그라핀 360',
            '익스트림 PRO 그라핀 360 플러스': '익스트림 PRO 그라핀 360 플러스',

        }

        img_name = img_names[self.name]

        return f"https://raw.githubusercontent.com/HiImYong/snrPictures/master/{img_name}.jpg"




class RacketDetail(models.Model):
    racket = models.OneToOneField(Racket, related_name='detail', on_delete=models.CASCADE)
    adminReview = models.TextField()
    adminPower = models.FloatField('운영자파워평점', default=0)
    adminSpin = models.FloatField('운영자스핀평점', default=0)
    adminManeuverability = models.FloatField('운영자조작성평점', default=0)
    adminStability = models.FloatField('운영자면안정성평점', default=0)
    adminComfort = models.FloatField('운영자안락함평점', default=0)
    adminAvgScore = models.FloatField('운영자평점평균', default=0)




