from django.forms import ModelForm
from .models import VisitorReview


class ReviewForm(ModelForm):
    # 모델 폼은 이너 클래스인 Meta 클래스가 반드시 필요하다.
    # Meta 클래스에는 사용할 모델과 모델의 속성을 적어야 한다.
    class Meta:
        model = VisitorReview
        fields = ['visitorReview', 'visitorScore']
        labels = {
            'visitorReview': '라켓 리뷰',
            'visitorScore': '라켓 점수'
        }

