import os
from io import BytesIO
from urllib.parse import urlparse
from urllib.request import urlopen

from django.contrib.auth import login
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.db import models

# Create your models here.
from django.db.models import QuerySet
from django.http import HttpRequest
from django.shortcuts import resolve_url


class User(AbstractUser):
    class loginType(models.TextChoices):
        GOOGLE = "google", "구글"
        KAKAO = "kakao", "카카오"

    providerType = models.CharField('연계 회원가입 기능 제공자인 프로바이더의 타입코드',
                                    max_length=20,
                                    choices=loginType.choices,
                                    default='unknown')

    providerAccountsId = models.PositiveIntegerField('연계 회원가입 기능 제공자인 프로바이더의 회원번호', default=0)

    name = models.CharField('이름', max_length=100)

    profile_img = models.ImageField('프로필이미지', blank=True, upload_to="accounts/profile_img/%Y/%m/%d",
                                    help_text="gif/png/jpg 이미지를 업로드해주세요.")
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)

    @staticmethod
    def dbRegisterAndLoginKakao(request: HttpRequest, account_id: int, provider_accounts_nickname: str,
                                provider_accounts_thumbnail_image_url: str):
        getProviderType = User.loginType.KAKAO
        qs: QuerySet = User.objects.filter(providerType=getProviderType, providerAccountsId=account_id)

        if qs.exists():
            user: User = qs.first()

        else:
            username = account_id
            name = provider_accounts_nickname if provider_accounts_nickname else username
            email = ""
            password = ""
            user: User = User.objects.create_user(username=username, email=email, password=password, name=name,
                                                  providerType=getProviderType, providerAccountsId=account_id)

            if provider_accounts_thumbnail_image_url:
                provider_accounts_thumbnail_image_url_parsed = urlparse(provider_accounts_thumbnail_image_url)
                provider_accounts_thumbnail_image_file_name = os.path.basename(
                    provider_accounts_thumbnail_image_url_parsed.path)

                response = urlopen(provider_accounts_thumbnail_image_url)
                io = BytesIO(response.read())
                user.profile_img.save(provider_accounts_thumbnail_image_file_name, File(io))

        login(request, user)

    # @property
    # def profile_img_url(self):
    #     if self.profile_img:
    #         return self.profile_img.url;
    #     return resolve_url('pydenticon_image', data=self.username)
