# django-mini-project
Django RESTFul API mini project

![PYTHON](https://img.shields.io/badge/Python-3.8.5-blue?logo=Python&logoColor=white)

### 1.가상환경 셋팅 및 서버 실행
```
$ virtualenv venv -p python3.8
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt 
(venv)$ python manage.py runserver
```

### 2. URL 설명

{type}
 - cbv - Class Based View로 작성한 로직
 - fbv - Function Based View로 작성한 로직
 - drf - DjangoRESTFramework로 작성한 로직

GET http://localhost:8000/api/{type}/restaurant - 음식점 리스트 가져오기

POST http://localhost:8000/api/{type}/restaurant - 음식점 새로 등록하기

GET http://localhost:8000/api/{type}/restaurant/{pk} - 음식점 상세보기

POST http://localhost:8000/api/{type}/restaurant/{pk}/menu - 메뉴 등록하기
