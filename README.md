# Django Tutorial
Django 튜토리얼 정리 자료

## 목차
- Part01. 요청과 응답
- Part02. 모델과 관리자 사이트
- Part03. 뷰와 템플릿
- Part04. 폼과 제네릭 뷰
- Part05. 테스트
- Part06. 정적 파일
- Part07. 관리자 사이트 커스터마이징
- Part08. 서드파티 패키지 추가
- Part09. 재사용 가능한 앱 만들기
- Part10. Django에 첫 번째 패치 작성

## Part01. 요청과 응답
`python -m pip install django`
Django를 설치.

`django-admin startproject [project_name] .`
이 명령어는 Django 프로젝트를 시작하기 위한 것. [project_name] 자리에는 프로젝트의 이름을 넣어주어야 함. 마침표(.)는 현재 디렉토리에서 프로젝트를 시작하라는 의미. 이 명령어를 실행하면 Django 프로젝트의 기본 구조가 생성되고, 설정 파일과 기본 앱이 함께 만들어짐.

`python manage.py runserver`
이 명령어는 개발 서버를 실행하는 것. Django 개발 서버는 개발 중인 웹 애플리케이션을 테스트하는 데 사용됨. 이 명령어를 실행하면 웹 서버가 시작되고, 개발 중인 Django 애플리케이션을 웹 브라우저에서 확인할 수 있음. 기본적으로 개발 서버는 http://127.0.0.1:8000/ 주소에서 실행됨.

`python manage.py startapp [app_name]`
이 명령어는 Django 앱을 생성하기 위한 것. [app_name] 자리에는 새로운 앱의 이름을 넣어주어야 함. 이 명령어를 실행하면 새로운 앱이 생성되고, 해당 앱의 기본 구조가 만들어짐. 앱은 Django 프로젝트 내에서 각각의 기능을 모듈화하고 구성하는 데 사용됨.
