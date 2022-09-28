from django.shortcuts import render
# random 모듈 가져오기
from random import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def travel(request):
    # 여행지 리스트 (장소를 추가해도 좋음)
    places = ["서울", "스위스", "이탈리아", "체코", "괌", "오스트리아"]

    # [코드 작성] pick 변수에 places 리스트 원소 중 하나 random으로 저장하기
    # 아래 줄에서 Ctrl + / 를 눌러 주석을 풀어준 후 코드 작성해주세요. 
    # pick = 

    # [코드 작성] context에 places와 pick을 딕셔너리로 저장하기
    # 딕셔너리 안쪽에서 Ctrl + / 를 눌러 "places"와 "pick"의 주석을 풀어준 후 코드 작성해주세요. 
    context = {
        # "places": ,
        # "pick": ,
    }

    return render(request, "travel.html", context)