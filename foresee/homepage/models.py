# -*- coding: utf-8 -*-
from django.db import models

# class Judgement(models.Model):
#     court = models.TextField(db_column='Court', blank=True, null=True)  # Field name made lowercase.
#     accidentdate = models.TextField(db_column='AccidentDate', blank=True, null=True)  # Field name made lowercase.
#     judgedate = models.TextField(db_column='JudgeDate', blank=True, null=True)  # Field name made lowercase.
#     assertionexisting = models.TextField(db_column='AssertionExisting', blank=True, null=True)  # Field name made lowercase.
#     judge = models.TextField(db_column='Judge', blank=True, null=True)  # Field name made lowercase.
#     judgefee = models.FloatField(db_column='JudgeFee', blank=True, null=True)  # Field name made lowercase.
#     judgereason = models.TextField(db_column='JudgeReason', blank=True, null=True)  # Field name made lowercase.
#     judgeid = models.TextField(db_column='JudgeId', blank=True, null=True)  # Field name made lowercase.
#     totaldamage = models.FloatField(db_column='TotalDamage', blank=True, null=True)  # Field name made lowercase.
#     pfee_dfee = models.TextField(db_column='PFee_DFee', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         # managed = False
#         db_table = 'judgement'
        
#modelManager

class Attribute(models.Model):
    judg_num = models.AutoField(primary_key=True)
    acc_date = models.DateField(blank=True, null=True)
    p_assertion = models.CharField(max_length=45, blank=True, null=True)
    d_assertion = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    judge = models.CharField(max_length=45, blank=True, null=True)
    judg_date = models.DateField(blank=True, null=True)
    judgefee = models.IntegerField(db_column='judgeFee', blank=True, null=True)  # Field name made lowercase.
    judgeid = models.CharField(db_column='judgeID', max_length=45)  # Field name made lowercase.
    judgereason = models.CharField(db_column='judgeReason', max_length=45, blank=True, null=True)  # Field name made lowercase.
    judgeresult = models.CharField(db_column='judgeResult', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pfee = models.IntegerField(db_column='pFee', blank=True, null=True)  # Field name made lowercase.
    dfee = models.IntegerField(db_column='dFee', blank=True, null=True)  # Field name made lowercase.
    total_damage = models.IntegerField(db_column='Total_Damage', blank=True, null=True)  # Field name made lowercase.
    inverstigation = models.CharField(max_length=45, blank=True, null=True)
    injured = models.CharField(max_length=45, blank=True, null=True)
    highway = models.CharField(max_length=45, blank=True, null=True)
    time = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'attribute'
        # unique_together = (('judg_num', 'judgeID'),)


class CrashType(models.Model):
    number = models.AutoField(primary_key=True)
    judgeid = models.CharField(db_column='judgeID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    crash_type = models.CharField(max_length=45, blank=True, null=True)
    judg_num = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'crash_type'
        # unique_together = (('judgeID', 'crash_type'),)


class Damageitem(models.Model):
    number = models.AutoField(primary_key=True)
    judgeid = models.CharField(db_column='judgeID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    item = models.CharField(max_length=45, blank=True, null=True)
    judg_num = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'damageitem'


class Lawyer(models.Model):
    number = models.AutoField(primary_key=True)
    judgeid = models.CharField(db_column='judgeID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pord = models.CharField(db_column='PorD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lawyer = models.CharField(max_length=45, blank=True, null=True)
    judg_num = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'lawyer'


class Situation(models.Model):
    number = models.AutoField(primary_key=True)
    judgeid = models.CharField(db_column='judgeID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    judgesituation = models.CharField(db_column='judgeSituation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    judg_num = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'situation'


class Vechical(models.Model):
    number = models.AutoField(primary_key=True)
    judgeid = models.CharField(db_column='judgeID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pord = models.CharField(db_column='PorD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cartype = models.CharField(db_column='carType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    judg_num = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'vechical'


class Weather(models.Model):
    number = models.AutoField(primary_key=True)
    judgeid = models.CharField(db_column='judgeID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    weather = models.CharField(max_length=45, blank=True, null=True)
    judg_num = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'weather'
