# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Attribute, Vechical, CrashType, Lawyer, Situation, Weather, Damageitem
from .forms import ConditionForm
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from operator import __or__ as OR
import time



def home(request):
	form = request.POST['judgefee']
	if form == '1000':
		j = Attribute.objects.filter(judgefee = 1000)
	else:
		j = Attribute.objects.exclude(judgefee = 1000)
	return render(request, 'base.html', {'j': j})

def myform(request):
	if request.method == 'POST':
		form = ConditionForm(request.POST)
		if form.is_valid():
			# return render(request, 'result', {'form': form})	
			return redirect('views.home', f=form.cleaned_data)
			# return HttpResponse(form.cleaned_data)
	else:
		form = ConditionForm()
	return render(request, 'form.html', {'form': form})	

def result(request):
	form = request.POST['judgefee']
	return render(request, 'result.html', {'form': form})

def create_post(request):
    # if request.method == 'POST':
    ts = time.time()
    # req = request.GET if request.method == 'GET' else request.POST

    judgefee = request.POST.get('judgefee') # test
    p_d = request.POST.get('p_d') # single
    court = request.POST.get('court') # single
    road_type = request.POST.get('road_type') # single
    injured_condition = request.POST.get('injured_condition') # single
    vel_me = request.POST.get('vel_me')
    vel_them = request.POST.get('vel_them')
    judge_situation = request.POST.get('judge_situation')
    crash_type = request.POST.get('crash_type')
    weather = request.POST.get('weather')


    # P or D
    me = p_d
    them = 'D' if me == 'P' else 'P'
    print 'me :'+me
    print 'them :'+them
    # single value(court, road_type, injured_condition)
    single_idset = set([])
    single_queryset = Attribute.objects.filter(Q(location = court), Q(highway = road_type), Q(injured = injured_condition))
    for i in single_queryset:
    	single_idset.add(i.judg_num)
    print len(single_idset)

    # # court
    # court_idset = set([])
    # court_quertset = Attribute.objects.filter(location = court)
    # for i in court_quertset:
    # 	court_idset.add(i.judgeid)
    # print len(court_idset)

    # # road_type
    # road_type_idset = set([])
    # road_type_quertset = Attribute.objects.filter(highway = road_type)
    # for i in road_type_quertset:
    # 	road_type_idset.add(i.judgeid)
    # print len(road_type_idset)

    # # injured_condition
    # injured_condition_idset = set([])
    # injured_condition_quertset = Attribute.objects.filter(injured = injured_condition)
    # for i in injured_condition_quertset:
    # 	injured_condition_idset.add(i.judgeid)
    # print len(injured_condition_idset)

    # vel_me
    vel_me_list = vel_me.split(',')
    vel_me_Qlist = []
    vel_me_idset = set([])
    for i in vel_me_list:
    	vel_me_Qlist.append(Q(cartype = i))
    vel_me_queryset = Vechical.objects.filter(Q(pord = me), reduce(OR, vel_me_Qlist))
    for i in vel_me_queryset:
    	vel_me_idset.add(i.judg_num)
    print len(vel_me_idset)

    # vel_them
    vel_them_list = vel_them.split(',')
    vel_them_Qlist = []
    vel_them_idset = set([])
    for i in vel_them_list:
    	vel_them_Qlist.append(Q(cartype = i))
    vel_them_queryset = Vechical.objects.filter(Q(pord = them), reduce(OR, vel_them_Qlist))
    for i in vel_them_queryset:
    	vel_them_idset.add(i.judg_num)
    print len(vel_them_idset)

    # judge_situation
    judge_situation_list = judge_situation.split(',')
    judge_situation_Qlist = []
    judge_situation_idset = set([])
    for i in judge_situation_list:
    	judge_situation_Qlist.append(Q(judgesituation = i))
    judge_situation_queryset = Situation.objects.filter(reduce(OR, judge_situation_Qlist))
    for i in judge_situation_queryset:
    	judge_situation_idset.add(i.judg_num)
    print len(judge_situation_idset)

    # crash_type
    crash_type_list = crash_type.split(',')
    crash_type_Qlist = []
    crash_type_idset = set([])
    for i in crash_type_list:
    	crash_type_Qlist.append(Q(crash_type = i))
    crash_type_queryset = CrashType.objects.filter(reduce(OR, crash_type_Qlist))
    for i in crash_type_queryset:
    	crash_type_idset.add(i.judg_num)
    print len(crash_type_idset)

    # weather
    weather_list = weather.split(',')
    weather_Qlist = []
    weather_idset = set([])
    for i in weather_list:
    	weather_Qlist.append(Q(weather = i))
    weather_queryset = Weather.objects.filter(reduce(OR, weather_Qlist))
    for i in weather_queryset:
    	weather_idset.add(i.judg_num)
    print len(weather_idset)

    multi_set = vel_me_idset.intersection(vel_them_idset).intersection(judge_situation_idset).intersection(crash_type_idset).intersection(weather_idset).intersection(single_idset)
    print len(multi_set), (i for i in multi_set)

    # queryset = Attribute.objects.filter(judg_num__in = list(multi_set)).values()[:100]

    if judgefee == '1000':
    	queryset = Attribute.objects.filter(judgefee = 1000).values()[:100]
    else:
    	queryset = Attribute.objects.exclude(judgefee = 1000).values()[:100]

    print judgefee, p_d, vel_me, vel_them, court, judge_situation, crash_type, weather, road_type, injured_condition
    return JsonResponse(dict(Attribute=list(queryset)))
    print ts - time.time()
    # return JsonResponse(serializers.serialize('json', queryset))
    # else:
    # return JsonResponse({"nothing to see": "this isn't happening"})

def show_summary(request, num):
    # judg_num = request.GET.get('judg_num') # test
	# print type(int(num))
	queryset = Attribute.objects.filter(judg_num = int(num)).values()
	# print num, queryset
	# return JsonResponse(queryset, safe=False)
	return JsonResponse(dict(Verdict=list(queryset)))

# def full_content(request):

# 	return render(request, 'verdict.html')