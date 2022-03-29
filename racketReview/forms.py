from django import forms
from django.forms import ModelForm
from .models import RacketReviewModel


# class ReviewForm(ModelForm):
#     # 모델 폼은 이너 클래스인 Meta 클래스가 반드시 필요하다.
#     # Meta 클래스에는 사용할 모델과 모델의 속성을 적어야 한다.
#     class Meta:
#         model = VisitorReview
#         fields = ['visitorReview']
#         labels = {
#             'visitorReview': '라켓 리뷰'
#         }

class ReviewForm(forms.Form):
    visitorReview = forms.CharField(
        max_length=100,
        label='한줄평',
        widget=forms.TextInput(attrs={
            'class': 'textReview',
        })
    )

    visitorScore = forms.IntegerField(
        label='한줄평',
        widget=forms.NumberInput(attrs={
            'class': 'scoreReview',
        })
    )

