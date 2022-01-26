from django.contrib import messages
from django.contrib.auth.views import logout_then_login
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
import requests

# Create your views here.
from account.models import User


def logOut(request: HttpRequest):
    messages.success(request, "로그아웃 되었습니다.")
    return logout_then_login(request, login_url='/racket')



def kakaoLogin(request: HttpRequest):
    client_id = "KAKAO_APP__REST_API_KEY"
    REDIRECT_URI = "KAKAO_APP__LOGIN__REDIRECT_URI"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={REDIRECT_URI}&response_type=code"
        # client_id를 통해 인증 코드 요청. 받아온 코드를 REDIRECT_URI로 전달.
    )


def kakaoLoginCallBack(request):
    code = request.GET.get("code")
    client_id = "KAKAO_APP__REST_API_KEY"
    REDIRECT_URI = "KAKAO_APP__LOGIN__REDIRECT_URI"

    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={REDIRECT_URI}&code={code}"
        # 인증 코드를 합쳐서 인증 토큰을 요청
    )

    token_json = token_request.json()

    error = token_json.get("error", None)
    if error is not None:
        raise KakaoException("에러가 발생하였습니다.")

    access_token = token_json.get("access_token")

    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"},
        # 가져온 토큰을 통해 API를 호출
    )
    profile_json = profile_request.json()
    # 유효성이 확인된 토큰에 대해 응답 전달

    account_id = profile_json.get("id")

    User.dbRegisterAndLoginKakao(request, account_id)

    messages.success(request, "카카오톡 계정으로 로그인되었습니다")

    return redirect("racket:racketMain")
