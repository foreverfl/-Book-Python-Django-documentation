from django.http import HttpResponse


def index(request):  # 웹 페이지의 루트 URL에 접근했을 때 실행되는 뷰 함수
    return HttpResponse("Hello, world. You're at the polls index.")
