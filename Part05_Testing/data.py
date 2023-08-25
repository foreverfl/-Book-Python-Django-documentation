import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # 프로젝트 설정에 필요한 환경 변수 설정
django.setup()  # Django 앱 초기화

from polls.models import Question, Choice
from django.utils import timezone

questions_data = [
    ("What's your favorite programming language?", ["Python", "Java", "C#"]),
    ("Do you like to travel?", ["Yes", "No", "Maybe"]),
    ("What's your favorite food?", ["Pizza", "Burger", "Salad"]),
    ("Do you prefer Android or iOS?", ["Android", "iOS", "Both"]),
    ("What's your favorite season?", ["Spring", "Summer", "Winter"])
]

for question_text, choices_text in questions_data:
    question = Question(question_text=question_text, pub_date=timezone.now())
    question.save()
    for choice_text in choices_text:
        choice = Choice(question=question, choice_text=choice_text, votes=0)
        choice.save()