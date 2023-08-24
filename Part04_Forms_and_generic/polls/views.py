from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def index(request):  # 웹 페이지의 루트 URL에 접근했을 때 실행되는 뷰 함수
#     # Question 모델에서 pub_date 필드를 기준으로 내림차순으로 정렬한 뒤, 최근 5개의 질문을 가져옴
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     logging.info(latest_question_list)
    
#     # 렌더링할 때 템플릿에 전달할 변수들을 담은 딕셔너리
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     # 템플릿을 렌더링하여 HTML 문서로 변환
#     return render(request, "polls/index.html", context)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self): # 모델을 지정함
        return Question.objects.order_by("-pub_date")[:]


# def detail(request, question_id):
#     # 해당 객체가 존재하지 않는 경우 404 에러 페이지를 보여줌
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        logging.info(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
