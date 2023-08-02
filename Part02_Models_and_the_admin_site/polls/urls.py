from django.urls import path  # URL 패턴과 뷰 함수를 연결하는 역할

from . import views  # 현재 패키지(현재 앱)에서 views.py 파일을 import

urlpatterns = [  # URL 패턴과 뷰 함수의 매핑을 설정하는 변수
    path("", views.index, name="index"),  # path() 함수를 이용하여 URL 패턴과 뷰 함수를 연결
]
