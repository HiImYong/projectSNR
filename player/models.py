from django.db import models


# Create your models here.
from account.models import User


class Player(models.Model):
    name = models.CharField('선수이름', max_length=20)
    birth = models.DateTimeField('생일', default="0000.00.00")
    turnPro = models.IntegerField('프로전향', default=0)
    weight = models.IntegerField('몸무게', default=0)
    height = models.FloatField('키', default=0)
    country = models.CharField('국가', max_length=20, default="등록전")
    forehand = models.CharField('포핸드사용손', max_length=20, default="등록전")
    backhand = models.CharField('백핸드종류', max_length=20, default="등록전")
    racketBrand = models.CharField('선수이름', max_length=20, default="등록전")
    racketUse = models.CharField('사용라켓', max_length=20, default="등록전")
    racketWeight = models.IntegerField('라켓무게', default=0)
    like = models.ManyToManyField(User, related_name='likePlayer')
    countLike = models.IntegerField('좋아요개수', default=0)


    def thumb_img_url(self):
        img_names = {
            '가엘 몽피스': '가엘 몽피스',
            '고란 이바니세비치': '고란 이바니세비치',
            '구스타브 쿠에르텡': '구스타브 쿠에르텡',
            '권순우': '권순우',
            '그레고리 디미트로프': '그레고리 디미트로프',
            '남지성': '남지성',
            '노박 조코비치': '노박 조코비치',
            '니시오카 요시히토': '니시오카 요시히토',
            '니시코리 게이': '니시코리 게이',
            '니콜라즈 바실라쉬빌리': '니콜라즈 바실라쉬빌리',
            '닉 키리오스': '닉 키리오스',
            '다니엘 에반스': '다니엘 에반스',
            '다닐 메드베데프': '다닐 메드베데프',
            '다비드 고핀': '다비드 고핀',
            '다비드 날반디안': '다비드 날반디안',
            '다비드 페러': '다비드 페러',
            '더스틴 브라운': '더스틴 브라운',
            '데니스 샤포발로프': '데니스 샤포발로프',
            '도미닉 티엠': '도미닉 티엠',
            '디에고 슈왈츠만': '디에고 슈왈츠만',
            '라파엘 나달': '라파엘 나달',
            '레이튼 휴이트': '레이튼 휴이트',
            '레일리 오펠카': '레일리 오펠카',
            '로렌조 무세티': '로렌조 무세티',
            '로렌조 소네고': '로렌조 소네고',
            '로베르토 바우티스타 아굿': '로베르토 바우티스타 아굿',
            '로이드 헤리스': '로이드 헤리스',
            '로저 페더러': '로저 페더러',
            '리차드 가스케': '리차드 가스케',
            '마라트 사핀': '마라트 사핀',
            '마르코스 바그다티스': '마르코스 바그다티스',
            '마린 칠리치': '마린 칠리치',
            '마이클 창': '마이클 창',
            '마츠 빌란데르': '마츠 빌란데르',
            '마크 필리포시스': '마크 필리포시스',
            '마테오 베레티니': '마테오 베레티니',
            '미카엘 이메르': '미카엘 이메르',
            '밀로스 라오니치': '밀로스 라오니치',
            '보르나 코리치': '보르나 코리치',
            '보리스 베커': '보리스 베커',
            '보틱 판더잘츠휠프': '보틱 판더잘츠휠프',
            '브랜돈 나카시마': '브랜돈 나카시마',
            '비외른 보리': '비외른 보리',
            '샘 쿼리': '샘 쿼리',
            '샘프라스': '샘프라스',
            '세바스티안 코르다': '세바스티안 코르다',
            '스타니슬라스 바브리카': '스타니슬라스 바브리카',
            '스테파노스 치치파스': '스테파노스 치치파스',
            '스테판 에드베리': '스테판 에드베리',
            '스티브 존슨': '스티브 존슨',
            '아슬란 카라트세브': '아슬란 카라트세브',
            '안드레 애거시': '안드레 애거시',
            '안드레아스 세피': '안드레아스 세피',
            '안드레이 루블레프': '안드레이 루블레프',
            '알렉산더 즈베레프': '알렉산더 즈베레프',
            '알렉스 드미노': '알렉스 드미노',
            '앤디 로딕': '앤디 로딕',
            '앤디 머리': '앤디 머리',
            '야닉 시너': '야닉 시너',
            '위고 가스통': '위고 가스통',
            '이반 렌들': '이반 렌들',
            '이보 카를로비치': '이보 카를로비치',
            '이형택': '이형택',
            '잭 속': '잭 속',
            '정현': '정현',
            '조 월프레드 송가': '조 월프레드 송가',
            '존 맥캔로': '존 맥캔로',
            '존 밀먼': '존 밀먼',
            '존 이스너': '존 이스너',
            '지미 코너스': '지미 코너스',
            '짐 쿠리어': '짐 쿠리어',
            '카렌 하차노프': '카렌 하차노프',
            '카를로스 모야': '카를로스 모야',
            '카를로스 알카라즈': '카를로스 알카라즈',
            '카메론 노리': '카메론 노리',
            '캐스퍼 루드': '캐스퍼 루드',
            '케빈 엔더슨': '케빈 엔더슨',
            '크리스티안 가린': '크리스티안 가린',
            '테일러 프리츠': '테일러 프리츠',
            '토마스 베르디흐': '토마스 베르디흐',
            '팀 헨만': '팀 헨만',
            '파블로 카레뇨 부스타': '파블로 카레뇨 부스타',
            '파비오 포그니니': '파비오 포그니니',
            '패트릭 래프터': '패트릭 래프터',
            '페르난도 곤잘레스': '페르난도 곤잘레스',
            '페르난도 베르다스코': '페르난도 베르다스코',
            '펠리치아노 로페즈': '펠리치아노 로페즈',
            '펠릭스 오거 알리아심': '펠릭스 오거 알리아심',
            '프란시스 티아포': '프란시스 티아포',
            '피에르위그 에르베르': '피에르위그 에르베르',
            '후안 마틴 델 포트로': '후안 마틴 델 포트로',
            '휴버트 후르카츠': '휴버트 후르카츠',
            '니콜라이 다비덴코': '니콜라이 다비덴코',
            '로빈 쇠덜링': '로빈 쇠덜링',
            '다니엘 유': '다니엘 유',
            '토미 하스': '토미 하스',
            '뤼카 푸유': '뤼카 푸유',
            '줄리앙 베네토': '줄리앙 베네토',
            '어네스트 굴비스': '어네스트 굴비스',
            '알렉세이 포피린': '알렉세이 포피린',
            '양상국': '양상국',
        }

        img_name = img_names[self.name]

        return f"https://raw.githubusercontent.com/HiImYong/snrPictures_players/master/{img_name}.jpg"


class playerCharacteristic(models.Model):
    Characteristic = models.CharField('선수특성', max_length=20)
    aboutCharacteristic = models.CharField('선수특성설명', max_length=20)
    playerJoin = models.ForeignKey(Player, related_name='Player', on_delete=models.CASCADE, default='')

    def thumb_img_url(self):
        img_names = {
            '메이저우승': '메이저우승',
            '메이저준우승': '메이저준우승',
            '백핸드마스터': '백핸드마스터',
            '분노': '분노',
            '대포알서브': '대포알서브',
            '스프린터': '스프린터',
            '스핀머신': '스핀머신',
            '엔터테이너': '엔터테이너',
            '아크로바틱': '아크로바틱',
            '뉴튜버': '뉴튜버',
            '잔디지배자': '잔디지배자',
            '컨트롤러': '컨트롤러',
            '클레이지배자': '클레이지배자',
            '통곡의벽': '통곡의 벽',
            '포핸드마스터': '포핸드마스터',
            '하드지배자': '하드지배자',
            '칼날발리': '칼날발리',
            '올라운더': '올라운더',
        }

        img_name = img_names[self.Characteristic]

        return f"https://raw.githubusercontent.com/HiImYong/snrPictures_players_characteristic/master/{img_name}.jpg"
