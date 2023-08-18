import os
import django
from django.utils import timezone
import datetime

# 프로젝트 설정에 필요한 환경 변수 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # 'myproject'는 프로젝트 이름으로 변경해야 합니다.

# Django 설정을 로드
django.setup()

from polls.models import Question, Choice  # 'polls'는 앱의 이름이므로 실제 앱 이름으로 변경해야 합니다.

# 질문과 선택사항을 정의하고 저장합니다.
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