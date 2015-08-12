# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Attribute, Vechical, CrashType, Lawyer, Situation, Weather, Damageitem, FullContent
from .forms import ConditionForm
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from operator import __or__ as OR
from operator import __and__ as AND
import time



def home(request):
	return render(request, 'index.html')

# def myform(request):
# 	if request.method == 'POST':
# 		form = ConditionForm(request.POST)
# 		if form.is_valid():
# 			# return render(request, 'result', {'form': form})	
# 			return redirect('views.home', f=form.cleaned_data)
# 			# return HttpResponse(form.cleaned_data)
# 	else:
# 		form = ConditionForm()
# 	return render(request, 'form.html', {'form': form})	

# def result(request):
# 	form = request.POST['judgefee']
# 	return render(request, 'result.html', {'form': form})

# def create_post(request):

def q_single(court, road_type, injured_condition, daypart):
    single_Qlist = []
    single_idset = set([])
    if (court != ''):
        single_Qlist.append(Q(location = court))
    else:
        print 'no court chosen'
    if (road_type != ''):
        single_Qlist.append(Q(highway = road_type))
    else:
        print 'no road_type chosen'
    if (injured_condition != ''):
        single_Qlist.append(Q(injured = injured_condition))
    else:
        print 'no injured_condition chosen'
    if (daypart != ''):
        single_Qlist.append(Q(time = daypart))
    else:
        print 'no daypart chosen'
    if (len(single_Qlist) != 0):
        single_queryset = Attribute.objects.filter(reduce(AND, single_Qlist))
        for i in single_queryset:
            single_idset.add(i.judg_num)
        print 'single_idset', len(single_idset)
    elif(len(single_Qlist) == 0):
        print 'single_Qlist', 0
    return single_idset

def q_vehicle_me(vel_me, me):
    vel_me_list = vel_me.split(',')
    vel_me_Qlist = []
    vel_me_idset = set([])
    for i in vel_me_list:
        vel_me_Qlist.append(Q(cartype = i))
    vel_me_queryset = Vechical.objects.filter(Q(pord = me), reduce(OR, vel_me_Qlist))
    for i in vel_me_queryset:
        vel_me_idset.add(i.judg_num)
    print 'vel_me_idset', len(vel_me_idset)
    return vel_me_idset

def q_vehicle_them(vel_them, them):
    vel_them_list = vel_them.split(',')
    vel_them_Qlist = []
    vel_them_idset = set([])
    for i in vel_them_list:
        vel_them_Qlist.append(Q(cartype = i))
    vel_them_queryset = Vechical.objects.filter(Q(pord = them), reduce(OR, vel_them_Qlist))
    for i in vel_them_queryset:
        vel_them_idset.add(i.judg_num)
    print 'vel_them_idset', len(vel_them_idset)
    return vel_them_idset

def q_judge_situation(judge_situation):
    judge_situation_list = judge_situation.split(',')
    judge_situation_Qlist = []
    judge_situation_idset = set([])
    for i in judge_situation_list:
        judge_situation_Qlist.append(Q(judgesituation = i))
    judge_situation_queryset = Situation.objects.filter(reduce(OR, judge_situation_Qlist))
    for i in judge_situation_queryset:
        judge_situation_idset.add(i.judg_num)
    print 'judge_situation_idset', len(judge_situation_idset)
    return judge_situation_idset

def q_crash_type(crash_type):
    crash_type_list = crash_type.split(',')
    crash_type_Qlist = []
    crash_type_idset = set([])
    if (crash_type_list[0] != ''):
        for i in crash_type_list:
            crash_type_Qlist.append(Q(crash_type = i))
        crash_type_queryset = CrashType.objects.filter(reduce(OR, crash_type_Qlist))
        for i in crash_type_queryset:
            crash_type_idset.add(i.judg_num)
        # id_set
        # multi_set = multi_set.intersection(crash_type_idset)
        print 'crash_type_idset', len(crash_type_idset)
    else:
        print 'no crash_type chosen'
    return crash_type_idset

def q_weather(weather):
    weather_list = weather.split(',')
    weather_Qlist = []
    weather_idset = set([])
    if (weather_list[0] != ''):
        for i in weather_list:
            weather_Qlist.append(Q(weather = i))
        weather_queryset = Weather.objects.filter(reduce(OR, weather_Qlist))
        for i in weather_queryset:
            weather_idset.add(i.judg_num)
        # id_set
        # multi_set = multi_set.intersection(weather_idset)
        print 'weather_idset', len(weather_idset)
    else:
        print 'no weather chosen'
    return weather_idset

def search_verdict(request):
    # if request.method == 'POST':
    # req = request.GET if request.method == 'GET' else request.POST

    judgefee = request.GET.get('judgefee') # test
    p_d = request.GET.get('p_d') # single
    court = request.GET.get('court') # single
    road_type = request.GET.get('road_type') # single
    injured_condition = request.GET.get('injured_condition') # single
    vel_me = request.GET.get('vel_me')
    vel_them = request.GET.get('vel_them')
    judge_situation = request.GET.get('judge_situation')
    crash_type = request.GET.get('crash_type')
    weather = request.GET.get('weather')
    daypart = request.GET.get('daypart')    

    # P or D
    me = p_d
    them = 'D' if me == 'P' else 'P'
    print 'me :'+me
    print 'them :'+them

    q_id_dic = {
    'single_idset': q_single(court, road_type, injured_condition, daypart),
    'vel_me_idset': q_vehicle_me(vel_me, me),
    'vel_them_idset': q_vehicle_them(vel_them, them),
    'judge_situation_idset': q_judge_situation(judge_situation),
    'crash_type_idset': q_crash_type(crash_type),
    'weather_idset': q_weather(weather)
    }

    # single value(court, road_type, injured_condition, daypart)
    # single_idset = q_single(court, road_type, injured_condition, daypart)
    single_idset = q_id_dic['single_idset']

    # vel_me
    # vel_me_idset = q_vehicle_me(vel_me, me)
    vel_me_idset = q_id_dic['vel_me_idset']

    # vel_them
    # vel_them_idset = q_vehicle_them(vel_them, them)
    vel_them_idset = q_id_dic['vel_them_idset']

    # judge_situation
    # judge_situation_idset = q_judge_situation(judge_situation)
    judge_situation_idset = q_id_dic['judge_situation_idset']

    # id_set
    if (len(single_idset) == 0):
        multi_set = vel_me_idset.intersection(vel_them_idset).intersection(judge_situation_idset)
    else:
        multi_set = single_idset.intersection(vel_me_idset).intersection(vel_them_idset).intersection(judge_situation_idset)

    # crash_type
    # crash_type_idset = q_crash_type(crash_type)
    crash_type_idset = q_id_dic['crash_type_idset']
    if (len(crash_type_idset) != 0):
        multi_set = multi_set.intersection(crash_type_idset)

    # weather
    # weather_idset = q_weather(weather)
    weather_idset = q_id_dic['weather_idset']
    if (len(weather_idset) != 0):
        multi_set = multi_set.intersection(weather_idset)

    # TESTING
    # if judgefee == '1000':
    #     queryset = Attribute.objects.filter(judgefee = 1000).values()[:77]
    # else:
    #     queryset = Attribute.objects.exclude(judgefee = 1000).values()[:77]
    # ls = []
    # for i in queryset:
    #     ls.append(i['judg_num'])
    # items = Damageitem.objects.filter(judg_num__in = ls).values('item')

    queryset = Attribute.objects.filter(judg_num__in = list(multi_set)).values()
    items = Damageitem.objects.filter(judg_num__in = list(multi_set)).values('item')
    print judgefee, p_d, vel_me, vel_them, court, judge_situation, crash_type, weather, road_type, injured_condition
    print len(multi_set)
    return JsonResponse(dict(Attribute=list(queryset), Ditems=list(items)))
    # return JsonResponse(serializers.serialize('json', queryset))
    # else:
    # return JsonResponse({"nothing to see": "this isn't happening"})


def show_summary(request, num):
    judgenum = int(num)
    queryset = Attribute.objects.filter(judg_num = judgenum).values()
    damageitems = Damageitem.objects.filter(judg_num = judgenum).values('item')
    lawyers_p = Lawyer.objects.filter(judg_num = judgenum, pord= 'P').values('lawyer')
    lawyers_d = Lawyer.objects.filter(judg_num = judgenum, pord= 'D').values('lawyer')
    return JsonResponse(dict(Verdict=list(queryset), Item=list(damageitems), LawyerP=list(lawyers_p), LawyerD=list(lawyers_d)))

def full_content(request, num):
	queryset = FullContent.objects.filter(judg_num = int(num)).values('content')
	return render(request, 'verdict.html', dict(Verdict=list(queryset)))