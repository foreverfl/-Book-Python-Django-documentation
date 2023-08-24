# [학습자료] Django Tutorial

## 목차
- [Part01. 요청과 응답](#Part01.-요청과-응답)
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
### Django를 설치
> ```bash
> python -m pip install django
> ```

### Django의 버전을 확인
> ```
> python -m django --version
> ```

### Django 프로젝트를 시작
> ```bash
> django-admin startproject [project_name] .
> ```
이 명령어는 Django 프로젝트를 시작하기 위한 것. [project_name] 자리에는 프로젝트의 이름을 넣어주어야 함. 마침표(.)는 현재 디렉토리에서 프로젝트를 시작하라는 의미. 이 명령어를 실행하면 Django 프로젝트의 기본 구조가 생성되고, 설정 파일과 기본 앱이 함께 만들어짐.

### 프로젝트 폴더의 구성
> - [project_name]은 프로젝트의 컨테이너. 그 이름은 Django에게 중요하지 않음. 원하는 이름으로 바꿀 수 있음.
> - manage.py: 이 Django 프로젝트와 다양한 방식으로 상호 작용할 수 있는 명령줄 유틸리티. django-admin 및 manage.pymanage.py 에 대한 모든 세부 정보를 읽을 수 있음.
> - mysite/: 프로젝트의 실제 Python 패키지. 그 이름은 가져오기 위해 사용해야 하는 Python 패키지 이름.
> - mysite/__init__.py: 이 디렉토리를 Python 패키지로 간주해야 함을 Python에 알리는 빈 파일. 
> - mysite/settings.py: 이 Django 프로젝트에 대한 설정/구성. Django 설정은 설정 작동 방식에 대해 모두 알려줌.
> - mysite/urls.py: 이 Django 프로젝트에 대한 URL 선언. Django 기반 사이트의 "목차".
> - mysite/asgi.py: 프로젝트를 제공하기 위한 ASGI 호환 웹 서버의 진입점. 
> - mysite/wsgi.py: 프로젝트를 제공하기 위한 WSGI 호환 웹 서버의 진입점. 

### asgi와 wsgi의 차이
#### wsgi
> - 장점
> 1. Python 웹 애플리케이션과 웹 서버 간의 표준 인터페이스.
> 2. 동기 방식으로 작동하며, HTTP와 HTTPS를 지원함.
> 3. gunicorn, uWSGI 같은 여러 WSGI 호환 웹 서버와 함께 사용할 수 있음.
> 
> - 단점
> 1. 웹소켓, HTTP/2 등의 비동기 프로토콜을 기본적으로 지원하지 않음.
> 2. 대부분의 동기 프레임워크와 잘 작동합니다만, 비동기 지원이 제한적일 수 있음.

#### asgi
> - 장점
> 1. WSGI의 확장으로, 비동기 지원을 추가한 인터페이스.
> 2. 웹소켓, HTTP/2 등 비동기 프로토콜을 지원함.
> 3. Daphne, uvicorn 같은 여러 ASGI 호환 웹 서버와 함께 사용할 수 있음.
> 
> - 단점
> 1. 비교적 새로운 기술이라, 호환성과 지원이 WSGI만큼 넓지 않을 수 있음.

### 개발 서버를 실행
> ```bash
> python manage.py runserver
> ```
이 명령어는 개발 서버를 실행하는 것. Django 개발 서버는 개발 중인 웹 애플리케이션을 테스트하는 데 사용됨. 이 명령어를 실행하면 웹 서버가 시작되고, 개발 중인 Django 애플리케이션을 웹 브라우저에서 확인할 수 있음. 기본적으로 개발 서버는 http://127.0.0.1:8000/ 주소에서 실행됨.

### 특정 포트에서 개발 서버를 실행
> ```bash
> python manage.py runserver 8080
> ```

### Django 앱을 생성
> ```bash
> python manage.py startapp [app_name]
> ```
이 명령어는 Django 앱을 생성하기 위한 것. 이 명령어를 실행하면 새로운 앱이 생성되고, 해당 앱의 기본 구조가 만들어짐. 앱은 Django 프로젝트 내에서 각각의 기능을 모듈화하고 구성하는 데 사용됨.

## Part02. 모델과 관리자 사이트
### settings.py
> #### DATABASES
> - ENGINE: 'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', 또는 'django.db.backends.oracle'.
> - NAME: 데이터베이스명. SQLite를 쓰고 있다면, 'BASE_DIR / 'db.sqlite3'과 같은 식으로 전체 경로를 입력해야함.
> 
> #### By default, INSTALLED_APPS contains the following apps, all of which come with Django:
> - django.contrib.admin: 관리자 사이트.
> - django.contrib.auth: 인증 시스템.
> - django.contrib.contenttypes: 컨텐츠 타입.
> - django.contrib.sessions: 세션 프레임워크.
> - django.contrib.messages: 메세징 프레임워크.
> - django.contrib.staticfiles: 정적파일 관리 프레임워크.

### 데이터베이스를 생성하거나 변경함
> ```bash
> python manage.py migrate
> ```
Django 프로젝트에서 데이터베이스를 생성하거나 변경하는데 사용되는 명령어. Django의 모델(Model)은 데이터베이스의 테이블과 매핑되는데, 이 명령어는 프로젝트의 모델 정의를 바탕으로 데이터베이스의 테이블을 생성하거나 변경하는 작업을 수행. Django의 모델은 models.py 파일에 정의되어 있으며, 이 파일에서 모델의 필드와 관계 등을 정의. migrate 명령어는 이러한 모델 정의를 바탕으로 데이터베이스 스키마를 자동으로 관리하여 테이블을 생성하거나 스키마를 변경하는 작업을 수행.

### 마이그레이션 파일을 생성
> ```bash
> python manage.py makemigrations [app_name]
> ```
이 명령어는 애플리케이션의 모델 변경 사항을 기반으로 마이그레이션 파일을 생성하는 작업을 수행. Django의 모델은 데이터베이스의 테이블과 매핑되는데, 모델에 변경 사항이 생기면 이를 데이터베이스에 반영하기 위해 마이그레이션 파일을 생성해야 함. makemigrations 명령어를 실행하면 애플리케이션에서 발생한 모델 변경 사항들에 대한 마이그레이션 파일들이 "[app_name]/migrations" 디렉토리에 생성됨. 각 마이그레이션 파일은 데이터베이스 스키마 변경에 필요한 작업들을 포함하고 있음.

### SQL문을 출력
> ```bash
> python manage.py sqlmigrate [app_name] [migrations_name]
> ```
이 명령어는 "polls" 애플리케이션의 첫 번째 마이그레이션 파일인 migrations_name에 대한 SQL 문을 출력하는 작업을 수행. sqlmigrate 명령어는 마이그레이션 파일의 변경 사항을 데이터베이스 스키마 변경 SQL로 변환하여 출력하는 역할을 함. 이를 통해 생성된 SQL 문을 확인할 수 있으며, 데이터베이스 스키마 변경이 어떤 SQL 쿼리로 이루어지는지 미리 확인할 수 있음.

### Interactive Python Shell 실행하기
> ```bash
> python manage.py shell
> ```
Django 프로젝트의 개발 쉘(Interactive Python Shell)을 실행하는 명령어. 이 쉘은 Django 프로젝트와 관련된 파이썬 코드를 대화형으로 실행하고 테스트하는데 사용됨.

### superuser 계정을 생성
> ```bash
> python manage.py createsuperuser
> ```
Django 프로젝트에서 관리자(superuser) 계정을 생성하는 명령어. 이 명령어를 실행하면 새로운 관리자 계정을 만들 수 있음.

## Part03. 뷰와 템플릿
### urls.py: URL 경로와 해당 경로에 대한 뷰 함수를 연결.
> - path("link", method, name)
> 1. "link": URL 패턴 문자열. 사용자가 이 경로로 접속하면 연결된 뷰 함수가 호출됨.
> 2. method: 해당 URL 패턴에 대한 뷰 함수.
> 3. name: URL 패턴에 별칭을 부여하여 템플릿 또는 뷰에서 쉽게 참조할 수 있음.

### views.py: 사용자의 요청을 처리하고 응답을 반환하는 뷰 함수나 클래스를 정의.
> - render(request, template.html, context)
> 1. request: 사용자의 요청 객체.
> 2. template.html: 렌더링할 템플릿 파일의 이름.
> 3. context: 템플릿에 전달할 변수들을 담은 딕셔너리.
> 
> - get_object_or_404(Model, pk=model_id): 특정 모델에서 주어진 조건을 만족하는 객체를 가져오거나, 객체가 없으면 404 오류를 발생시킴.
> 1. Model: 조회할 모델 클래스.
> 2. pk: 조회할 객체의 기본 키 값.
> 3. model_id: 조회할 객체의 기본 키 값으로 사용됨.

### {% %} 태그: template.html에서 동적으로 HTML을 생성.
> - 변수 출력: {{ }} 태그를 사용하여 변수의 값을 출력할 수 있음. 예를 들어, {{ variable }}는 variable 변수의 값을 템플릿에 표시함.
> - 조건문: {% if %}와 {% else %} 태그를 사용하여 조건문을 처리할 수 있음. 특정 조건에 따라 템플릿의 일부를 보여주거나 숨길 수 있음.
> - 반복문: {% for %}와 {% endfor %} 태그를 사용하여 반복문을 처리할 수 있음. 리스트나 쿼리셋 등과 같은 반복 가능한 객체의 각 요소에 대해 템플릿을 반복하여 렌더링할 수 있음.
> - 주석: {# #} 태그를 사용하여 주석을 작성할 수 있음. 주석은 템플릿 엔진에 의해 무시되며, 템플릿 코드에 설명을 추가할 때 유용함.
> - 기타: {% url %}, {% include %}, {% block %}, {% extends %} 등 다양한 기능을 제공함.

## Part04. 폼과 제네릭 뷰
## Part05. 테스트
## Part06. 정적 파일
## Part07. 관리자 사이트 커스터마이징
## Part08. 서드파티 패키지 추가
## Part09. 재사용 가능한 앱 만들기
## Part10. Django에 첫 번째 패치 작성
