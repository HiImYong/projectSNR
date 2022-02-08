from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField('선수이름', max_length=20)
    birth = models.DateTimeField('생일', default="0000.00.00")
    trunPro = models.IntegerField('프로전향', default=0)
    weight = models.IntegerField('몸무게', default=0)
    height = models.FloatField('키', default=0)
    contury = models.IntegerField('국가', default=0)
    forehand = models.IntegerField('포핸드위치', default=0)
    backhand = models.CharField('백핸드종류', max_length=20, default="등록전")
    racketBrand = models.CharField('선수이름', max_length=20, default="등록전")

    def thumb_img_url(self):
        img_names = {
            1: '가엘 몽피스',
            2: '권순우',
            3: '그레고리 디미트로프',
            4: '남지성',
            5: '노박 조코비치',
            6: '니시오카',
            7: '니시코리',
            8: '니콜라즈 바실라쉬빌리',
            9: '닉 키리오스',
            10: '다니엘 에반스',
            11: '다닐 메드베데프',
            12: '다비드 고핀',
            13: '다비드 날반디안',
            14: '다비드 페러',
            15: '더스틴 브라운',
            16: '데니스 샤포발로프',
            17: '후안 마틴 델 포트로',
            18: '도미닉 티엠',
            19: '디에고 슈왈츠만',
            20: '라파엘 나달',
            21: '레이튼 휴이트',
            22: '레일리 오펠카',
            23: '로렌조 무세티',
            24: '로렌조 소네고',
            25: '로베르토 바우티스타 아굿',
            26: '로이드 헤리스',
            27: '로저 페더러',
            28: '리차드 가스케',
            29: '마린 칠리치',
            30: '마테오 베레티니',
            31: '미카엘 이메르',
            32: '밀로스 라오니치',
            33: '보르나 코리치',
            34: '보틱 판더잘츠휠프',
            35: '브랜돈 나카시마',
            36: '샘 쿼리',
            37: '샘프라스',
            38: '세바스티안 코르다',
            39: '스타니슬라스 바브리카',
            40: '스테파노스 치치파스',
            41: '스테판 에드베리',
            42: '스티브 존슨',
            43: '아슬란 카라트세브',
            44: '안드레 애거시',
            45: '안드레아스 세피',
            46: '안드레이 루블레프',
            47: '알렉산더 즈베레프',
            48: '알렉스 드미노',
            49: '앤디 로딕',
            50: '앤디 머리',
            51: '야닉 시너',
            52: '위고 가스통',
            53: '이반 렌들',
            54: '이보 카를로비치',
            55: '이형택',
            56: '정현',
            57: '조 월프레드 송가',
            58: '존 맥캔로',
            59: '존 밀먼',
            60: '존 이스너',
            61: '지미 코너스',
            62: '카렌 하차노프',
            63: '카를로스 알카라즈',
            64: '카메론 노리',
            65: '캐스퍼 루드',
            66: '케빈 엔더슨',
            67: '크리스티안 가린',
            68: '테일러 프리츠',
            69: '팀 헨만',
            70: '파블로 카레뇨 부스타',
            71: '파비오 포그니니',
            72: '페르난도 곤잘레스',
            73: '페르난도 베르다스코',
            74: '펠리치아노 로페즈',
            75: '펠릭스 오거 알리아심',
            76: '프란시스 티아포',
            77: '피에르위그 에르베르',
            78: '휴버트 후르카츠',
            79: '잭 속',
        }

        img_name = img_names[self.id]

        return f"https://raw.githubusercontent.com/HiImYong/snrPictures_players/master/{img_name}.jpg"
