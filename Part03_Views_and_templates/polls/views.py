from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question


def index(request):  # 웹 페이지의 루트 URL에 접근했을 때 실행되는 뷰 함수
    # Question 모델에서 pub_date 필드를 기준으로 내림차순으로 정렬한 뒤, 최근 5개의 질문을 가져옴
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # 렌더링할 때 템플릿에 전달할 변수들을 담은 딕셔너리
    context = {"latest_question_list": latest_question_list}
    # 템플릿을 렌더링하여 HTML 문서로 변환
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # 해당 객체가 존재하지 않는 경우 404 에러 페이지를 보여줌
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
