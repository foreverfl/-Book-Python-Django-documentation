from django.contrib import admin

from .models import Question

admin.site.register(Question) # admin 페이지에서 모델을 관리할 수 있도록 함
