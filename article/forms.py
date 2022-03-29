from django import forms
from .models import Article


# class ArticleFrom(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ['subject', 'content']

class ArticleForm(forms.Form):
    articleSubject = forms.CharField(
        max_length=50,
        label='질문제목',
        widget=forms.TextInput(attrs={
            'class': 'articleSubject',
        })
    )

    articleContent = forms.CharField(
        max_length=300,
        label='질문내용',
        widget=forms.TextInput(attrs={
            'class': 'articleContent',
        })
    )


class ReplyForm(forms.Form):
    replyContent = forms.CharField(
        max_length=300,
        label='답글내용',
        widget=forms.TextInput(attrs={
            'class': 'replyContent',
        })
    )
