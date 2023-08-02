"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin  # Django의 관리자 페이지를 사용하기 위한 모듈
from django.urls import include  # 다른 URL 패턴을 포함
from django.urls import path  # 함수는 URL 패턴과 뷰를 연결하는 데 사용됨

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),  # Django의 관리자 사이트 URL
]
