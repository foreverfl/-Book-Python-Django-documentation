import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuestionModelTests(TestCase):
    # 질문의 발행 날짜가 미래인 경우를 테스트 
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30) # 현재 시간에서 30일 후의 시간을 계산
        future_question = Question(pub_date=time) # pub_date가 30일 후인 Question 객체를 생성
        self.assertIs(future_question.was_published_recently(), False) # 메서드가 False를 반환하는지 확인
        
    # 질문의 발행 날짜가 1일보다 오래된 경우를 테스트 
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    # 질문의 발행 날짜가 최근 1일 이내인 경우를 테스트
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
        
# days가 양수인 경우 미래에 발행될 질문, 음수인 경우 과거에 발행된 질문을 생성
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    # 질문이 없는 경우 적절한 메시지가 표시되는지 테스트
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    # 과거의 질문을 테스트
    def test_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    # 미래의 질문을 테스트
    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    # 과거와 미래의 질문이 모두 있을 때, 오직 과거의 질문만 표시되는지 테스트
    def test_future_question_and_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30) # 동일하지 테스트는 하지 않기 때문에 변수로 저장하지 않음
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    # 인덱스 페이지가 여러 개의 과거 질문을 표시할 수 있는지 테스트
    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )
        
        
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)