from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from article.forms import ArticleForm, ReplyForm
from article.models import Article, Reply


def articleMain(request: HttpRequest):
    getArticle = Article.objects.all()
    return render(request, "article/article.html", {'articleItems': getArticle})


def articleCreate(request):
    if request.method == "POST":
        getForm = ArticleForm(request.POST)
        if getForm.is_valid():
            getInputSubject = getForm.cleaned_data['articleSubject']
            getInputContent = getForm.cleaned_data['articleContent']
            Article.objects.create(subject=getInputSubject, content=getInputContent, visitorAccount=request.user)
            messages.success(request, "게시글이 등록되었습니다")
            return redirect('article:articleMain')

        else:
            return redirect('article:articleMain')

    else:
        return render(request, "article/articleForm.html")


def articleContent(request, parameter):
    getArticleQs = Article.objects.filter(id=parameter)
    getReply = Reply.objects.filter(articleForeignKey_id=parameter)
    getArticle = getArticleQs.first()
    return render(request, "article/articleContent.html", {'articleItems': getArticle,
                                                           'replyItems': getReply})


def replyCreate(request, parameter):
    if request.method == "POST":
        getForm = ReplyForm(request.POST)
        if getForm.is_valid():
            getInputSubject = getForm.cleaned_data['replySubject']
            getInputContent = getForm.cleaned_data['replyContent']
            Reply.objects.create(subject=getInputSubject, articleForeignKey_id=parameter,
                                 content=getInputContent, visitorAccount=request.user)
            messages.success(request, "답글이 등록되었습니다")
            return redirect('article:articleContent', parameter)

        else:
            return redirect('article:articleContent', parameter)

    else:
        return redirect('article:articleContent', parameter)