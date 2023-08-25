from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):  # Model 클래스를 상속받아 데이터베이스 모델을 정의
    question_text = models.CharField(max_length=200)  # 열의 길이를 최대 200으로 제한
    pub_date = models.DateTimeField("date published")  # 열에 날짜와 시간을 저장함

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE)  # 외래키 설정(일대다 관계)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

