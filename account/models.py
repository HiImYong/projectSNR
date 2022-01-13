from django.contrib.auth import login
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import QuerySet
from django.http import HttpRequest


class User(AbstractUser):
    class loginType(models.TextChoices):
        GOOGLE = "google", "구글"
        KAKAO = "kakao", "카카오"

    providerType = models.CharField('연계 회원가입 기능 제공자인 프로바이더의 타입코드',
                                          max_length=20,
                                          choices=loginType.choices,
                                          default='unknown')
    providerAccountsId = models.PositiveIntegerField('연계 회원가입 기능 제공자인 프로바이더의 회원번호', default=0)


    @staticmethod
    def dbRegisterAndLoginKakao(request: HttpRequest, account_id):
        getProviderType = User.loginType.KAKAO
        qs: QuerySet = User.objects.filter(providerType=getProviderType, providerAccountsId=account_id)

        if qs.exists():
            user: User = qs.first()

        else:
            username = getProviderType + "__" + str(account_id)
            name = getProviderType + "__" + str(account_id)
            email = ""
            password = ""
            user: User = User.objects.create_user(username=username,
                                                  email=email,
                                                  password=password,
                                                  first_name=name,
                                                  providerType=getProviderType,
                                                  providerAccountsId=account_id)
        login(request, user)




