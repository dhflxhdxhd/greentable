from django.shortcuts import render
from .models import Place,Question,Choice
# from django.http import HttpResponse
from random import randint


def index(request):
    places = Place.objects.all()

    context = {
        'places' : places,
    }
    return render(request,'index.html',context=context)

def form(request):
    questions = Question.objects.all()

    context = {
        'questions' : questions,
    }

    return  render(request,'form.html',context=context)

def result(request):
    print(f' POST: {request.POST}')
    N = Question.objects.count()
    ques = []
    for n in range(1, N+1):
        place_type =  int(request.POST[f'question-{n}'][0])
        ques.append(place_type)


    # place_q1 = Place.objects.filter(division=ques[0])
    # place_q2 = Place.objects.filter(country=ques[1])
    # place_q3 = Place.objects.filter(explain=ques[2])
    final_place = Place.objects.filter(division=ques[0],
                                       country=ques[1],
                                       explain=ques[2])
    # print(final_place)
    # print("총 개수 : " + str(final_place.count()))  #final_place.cout() -> filter된 값의 총 개수

    # 값이 존재하지 않을 경우 제외 패턴 생성.
    # if(final_place.count() == ""):
    #     final_placenum = 0
    # else :

    final_placenum = randint(0, final_place.count())  # 랜덤 번호





    final_placeID = final_place[final_placenum].id # 선택된 장소의 id값
    print(final_place[final_placenum].id)
    final_get = Place.objects.get(id=final_placeID)

    context = {
        'finals' : final_place,
        'name' : final_place[final_placenum],
        'explain' : final_get.explain,
        'division' : final_get.division,
        'country' : final_get.country,
        'call' : final_get.call,
        'locate' : final_get.locate,
        'break' : final_get.day_break,
        'time' : final_get.time,
        'menu' : final_get.menu,
        'etc' : final_get.etc
    }
    return  render(request,'result.html',context=context)

def map(request):
    places = Place.objects.all()
    # one = Place.objects.get(id=1)
    # print(one.name)
    context = {
        'places' : places,
    }
    return render(request,'map.html',context=context)

def information(request):

    return render(request, 'information.html')