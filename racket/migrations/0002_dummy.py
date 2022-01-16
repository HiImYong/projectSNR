from django.db import migrations

from racket.models import Racket, RacketDetail


def gen_master(apps, schema_editor):
    Racket(name="블레이드 98 덴스", weight=305, pattern="18 : 20", headsize=98, length=27, balance=320, regDateInt=2021,
           manufacturer="WILSON").save()
    Racket(name="퓨어 드라이브", weight=300, pattern="16 : 19", headsize=100, length=27, balance=330, regDateInt=2019,
           manufacturer="BABOLAT").save()
    Racket(name="퓨어 에어로", weight=300, pattern="16 : 19", headsize=100, length=27, balance=330, regDateInt=2019,
           manufacturer="BABOLAT").save()
    Racket(name="스피드 프로", weight=310, pattern="18 : 20", headsize=100, length=27, balance=310, regDateInt=2020,
           manufacturer="HEAD").save()
    Racket(name="프레스티지 프로", weight=320, pattern="18 : 20", headsize=98, length=27, balance=310, regDateInt=2021,
           manufacturer="HEAD").save()
    Racket(name="그래비티 투어", weight=315, pattern="18 : 20", headsize=100, length=27, balance=310, regDateInt=2021,
           manufacturer="HEAD").save()
    Racket(name="프로스태프 97 RF", weight=340, pattern="16 : 19", headsize=97, length=27, balance=305, regDateInt=2021,
           manufacturer="WILSON").save()
    Racket(name="라디칼 프로", weight=315, pattern="16 : 19", headsize=98, length=27, balance=315, regDateInt=2020,
           manufacturer="HEAD").save()

    RacketDetail(racket_id=1, adminReview="괜찮은 라켓입니다.", adminPower="3", adminSpin="3", adminManeuverability="3",
                 adminStability="4", adminComfort="4").save()
    RacketDetail(racket_id=2, adminReview="강력한 파워형 라켓", adminPower="3", adminSpin="4", adminManeuverability="3",
                 adminStability="5", adminComfort="1").save()
    RacketDetail(racket_id=3, adminReview="무서운 스핀성능", adminPower="4", adminSpin="5", adminManeuverability="3",
                 adminStability="3", adminComfort="3").save()
    RacketDetail(racket_id=4, adminReview="다재다능한 라켓", adminPower="4", adminSpin="3", adminManeuverability="2",
                 adminStability="3", adminComfort="4").save()
    RacketDetail(racket_id=5, adminReview="로저 페더러의 유산", adminPower="3", adminSpin="3", adminManeuverability="2",
                 adminStability="2", adminComfort="4").save()
    RacketDetail(racket_id=6, adminReview="진짜 프로의 라켓", adminPower="4", adminSpin="2", adminManeuverability="3",
                 adminStability="3", adminComfort="4").save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('racket', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(gen_master)
    ]
