from django.db import migrations

from racket.models import Racket, RacketDetail


def gen_master(apps, schema_editor):

    RacketDetail(racket_id=1, adminReview="괜찮은 라켓입니다. 파워와 컨트롤을 둘다 골고루 가진 똑똑한 라켓입니다. "
                                          "약간의 무게감이 문제였지만 이번 버전에선 발란스가 일부 조정되었습니다."
                                          "이것저것 라켓 고르는데 힘들다면, 거의 실패없는 라켓이라고 할 수 있습니다."
                                          "색상에 대해선 호불호가 나뉘겠네요!", adminPower="3", adminSpin="3", adminManeuverability="3",
                 adminStability="4", adminComfort="4").save()
    RacketDetail(racket_id=2, adminReview="바볼랏의 강력한 파워형 모델이 돌아왔습니다."
                                          "기본 반발력이 너무 강력하지만 어느정도 스핀도 갖추고 있습니다."
                                          "그러나 그것으론 부족해요. 파워를 제어하려면 사용자가 드라이브를 의식하고 있어야 합니다."
                                          "퓨어 드라이브란 그런 라켓이니까요.", adminPower="3", adminSpin="4", adminManeuverability="3",
                 adminStability="5", adminComfort="1").save()
    RacketDetail(racket_id=3, adminReview="바볼랏의 노란 스핀머신입니다."
                                          "강력한 반발력을 바탕으로 높은 스핀 성능도 지니고 있습니다."
                                          "라켓의 프레임 모양이 수평 스윙을 강제하여 스핀성 공을 유도합니다."
                                          "하지만 역시 사용자가 드라이브를 걸 수 있는 능력이 있다는 가정하입니다 :)"
                                          "빔 두께에 대비해 조작성이 크게 나쁘지 않습니다.", adminPower="4", adminSpin="5", adminManeuverability="3",
                 adminStability="3", adminComfort="3").save()
    RacketDetail(racket_id=4, adminReview="다재다능한 라켓입니다."
                                          "어느정도 파워와 좋은 조작성을 가지고 있습니다."
                                          "다만 스핀성능이 약간 떨어지지만 덴스패턴 라켓 치고 이정도면 괜찮아요!"
                                          "라켓이 살짝 딱딱하다는 의견이 있습니다."
                                          "흑백의 디자인이 참 잘 나온 것 같네요.", adminPower="4", adminSpin="3", adminManeuverability="2",
                 adminStability="3", adminComfort="4").save()
    RacketDetail(racket_id=5, adminReview="전통의 프레스티지 MP라인이 PRO로 이름이 바뀌었습니다."
                                          "고컨트롤에 치중한 라켓. 98빵에 덴스패턴은 바뀌지 않아요."
                                          "시대가 갈 수록 파워가 늘어나는 것 같습니다."
                                          "평가가 아주 좋지만 도색에 문제가 있다고 하네요.", adminPower="3", adminSpin="3", adminManeuverability="2",
                 adminStability="2", adminComfort="4").save()
    RacketDetail(racket_id=6, adminReview="진정한 프로의 라켓."
                                          "리코치와 스카이코치가 좋아하는 라켓으로 유명합니다."
                                          "얇은 컨트롤성 프레임이 전형적인 클래식 라켓입니다."
                                          "그런데 중고나라에 매물이 쏟아지는 것을 보니 모두에게 맞지는 않나 봅니다."
                                          "사용자의 능력이 뒷받침되지 않으면 그저 그런 라켓이라고 할 수 있습니다.", adminPower="4", adminSpin="2", adminManeuverability="3",
                 adminStability="3", adminComfort="4").save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('racket', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(gen_master)
    ]
