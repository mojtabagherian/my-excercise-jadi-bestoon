# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense, Income
from datetime import datetime
# Create your views here.
@csrf_exempt
def submit_income(request):
    """user submit an income"""
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Income.objects.create(user = this_user, amount=request.POST['amount'],
             text = request.POST['text'], date = date)


@csrf_exempt
def submit_expense(request):
    """user submit an expense"""
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Expense.objects.create(user = this_user, amount=request.POST['amount'],
             text = request.POST['text'], date = date)


    return JsonResponse({
    'status':'ok',
    },encoder=JSONEncoder)
