from django.urls import path
# 같은 폴더 내의 views.py 파일 불러오기
from . import views

urlpatterns = [
    path('index/', views.index),
    # [코드 작성] views.py의 travel 함수를 실행해주는 url 생성하기
    path('travel/', ),
]