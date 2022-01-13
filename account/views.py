from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
import requests



# Create your views here.
from account.models import User


def kakaoLogin(request: HttpRequest):
    client_id = "d86505a159546cfa6120dae8ce274ead"
    REDIRECT_URI = "http://localhost:8000/account/kakaoLoginCallBack"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={REDIRECT_URI}&response_type=code"
        # client_id를 통해 인증 코드 요청. 받아온 코드를 REDIRECT_URI로 전달.
    )

def kakaoLoginCallBack(request):
    code = request.GET.get("code")
    client_id = "d86505a159546cfa6120dae8ce274ead"
    REDIRECT_URI = "http://localhost:8000/account/kakaoLoginCallBack"

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
    )
    profile_json = profile_request.json()

    account_id = profile_json.get("id")

    User.dbRegisterAndLoginKakao(request, account_id)

    messages.success(request, "카카오톡 계정으로 로그인되었습니다")

    return redirect("racket:racketMain")
