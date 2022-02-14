from django import forms
from django.forms import ModelForm


class ReviewForm(forms.Form):
    # 모델 폼은 이너 클래스인 Meta 클래스가 반드시 필요하다.
    # Meta 클래스에는 사용할 모델과 모델의 속성을 적어야 한다.
    visitorReview = forms.CharField(
        max_length=100,
        label='한줄평',
        widget=forms.TextInput(attrs={
            'class': 'textReview',
        })
    )
