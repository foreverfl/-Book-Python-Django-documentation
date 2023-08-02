from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


# 제레릭 뷰
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"  # 템플릿으로 넘겨줄 컨텍스트 변수의 이름

    def get_queryset(self):  # 템플릿으로 넘겨줄 쿼리셋
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",  # 렌더링할 템플릿 파일의 경로
            {
                # 컨텍스트 변수
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # reverse 함수는 URL 패턴 이름을 기반으로 URL을 생성
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
