"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('aboutSNR/', views.aboutSNR, name="aboutSNR"),
    path('racket/', include('racket.urls')),
    path('account/', include('account.urls')),
    path('racketReview/', include('racketReview.urls')),
    path('player/', include('player.urls')),
    path('playerReview/', include('playerReview.urls')),
    path('feedbackSNR/', include('feedback.urls')),
    path('article/', include('article.urls')),

]


if settings.DEBUG:

    # 미디어 파일 추가를 위해
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)