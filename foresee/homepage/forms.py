# -*- coding: utf-8 -*-
from django import forms

P_D_Choice = (
	('P', 'Plaintiff'),
	('D', 'Defendant'),
)

JudgeFee_Choice = (
	('1000', '1000'),
	('not1000', 'not1000'),
)

Vehicle_Choice = (
    ('小客車', '小客車'),
    ('營業小客車', '營業小客車'),
    ('重型機車', '重型機車'),
    ('卡車', '卡車'),
    ('火車', '火車'),
    ('輕型機車', '輕型機車'),
    ('大客車', '大客車'),
    ('腳踏車', '腳踏車'),
    ('三輪車', '三輪車'),
    ('拖板車', '拖板車'),
    ('農用車', '農用車'),
    ('行人', '行人'),
)

Court_Choice = (
	('基隆', '基隆'),
	('臺北', '臺北'),
	('士林', '士林'),
	('新北', '新北'),
	('桃園', '桃園'),
	('新竹', '新竹'),
	('苗栗', '苗栗'),
	('台中', '台中'),
	('彰化', '彰化'),
	('南投', '南投'),
	('雲林', '雲林'),
	('嘉義', '嘉義'),
	('臺南', '臺南'),
	('高雄', '高雄'),
	('屏東', '屏東'),
	('宜蘭', '宜蘭'),
	('花蓮', '花蓮'),
	('臺東', '臺東'),
	('澎湖', '澎湖'),
	('金門', '金門'),
	('連江', '連江'),
)

Judge_Situation_Choice = (
	('方向不當', '方向不當'),
	('忽略周圍狀況', '忽略周圍狀況'),
	('緊急煞車', '緊急煞車'),
	('未減速', '未減速'),
	('開啟車門', '開啟車門'),
	('違停', '違停'),
	('違反路權', '違反路權'),
	('違反號誌標線等', '違反號誌標線等'),
	('無安全車距', '無安全車距'),
	('車況不良', '車況不良'),
	('車輛不受控制', '車輛不受控制'),
	('駕駛精神不佳', '駕駛精神不佳'),
	('違規轉彎', '違規轉彎'),
	('行人違規', '行人違規'),
	('視線受阻', '視線受阻'),
	('方向不定', '方向不定'),
	('使用手機', '使用手機'),
	('搶道', '搶道'),
	('裝載違規', '裝載違規'),
	('號誌狀況不明', '號誌狀況不明'),
	('腳踏車違規附載坐人', '腳踏車違規附載坐人'),
)

Crash_Type_Choice = (
	('對撞', '對撞'),
	('追撞', '追撞'),
	('擦撞', '擦撞'),
	('倒車撞', '倒車撞'),
	('側撞', '側撞'),
	('推撞', '推撞'),
)

Weather_Choice = (
	('晴', '晴'),
	('雨', '雨'),
	('陰', '陰'),
	('高溫', '高溫'),
	('霧', '霧'),
	('強風', '強風'),
	('昏暗', '昏暗'),
	('日間', '日間'),
	('夜間', '夜間'),
)

Road_Type_Choice = (
	('一般道路', '一般道路'),
	('快速道路', '快速道路'),
)

Injured_Condition_Choice = (
	('死亡', '死亡'),
	('沒死亡有受傷', '沒死亡有受傷'),
	('未受傷', '未受傷'),
)

class ConditionForm(forms.Form):
	p_d = forms.ChoiceField(label = 'P_D', widget = forms.RadioSelect, choices = P_D_Choice)
	judgefee = forms.ChoiceField(label = 'JudgeFee', widget = forms.RadioSelect, choices = JudgeFee_Choice)
	vehicle_me = forms.MultipleChoiceField(label = 'Vehicle', widget=forms.CheckboxSelectMultiple, choices=Vehicle_Choice)
	vehicle_them = forms.MultipleChoiceField(label = 'Vehicle', widget=forms.CheckboxSelectMultiple, choices=Vehicle_Choice)
	court = forms.ChoiceField(label = 'Court', widget = forms.RadioSelect, choices = Court_Choice)
	judge_situation = forms.MultipleChoiceField(label = 'Judge_Situation', widget=forms.CheckboxSelectMultiple, choices=Judge_Situation_Choice)
	crash_type = forms.ChoiceField(label = 'Crash_Type', widget = forms.RadioSelect, choices = Crash_Type_Choice)
	weather = forms.MultipleChoiceField(label = 'Weather', widget=forms.CheckboxSelectMultiple, choices=Weather_Choice)
	road_type = forms.ChoiceField(label = 'Road_Type', widget = forms.RadioSelect, choices = Road_Type_Choice)
	injured_condition = forms.ChoiceField(label = 'Injured_Condition', widget = forms.RadioSelect, choices = Injured_Condition_Choice)
