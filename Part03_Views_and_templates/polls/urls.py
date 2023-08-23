from django.urls import path  # URL 패턴과 뷰 함수를 연결하는 역할
from . import views  # 현재 패키지(현재 앱)에서 views.py 파일을 import

app_name = "polls"
urlpatterns = [  # URL 패턴과 뷰 함수의 매핑을 설정하는 변수
    # ex: /polls/
    path("", views.index, name="index"),  # path() 함수를 이용하여 URL 패턴과 뷰 함수를 연결

    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),

    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),

    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
