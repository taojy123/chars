# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from models import *
import os
import uuid

def index(request):
    if Char.objects.filter(level=1):
        one = Char.objects.filter(level=1)[0]
    else:
        one = Char(level=1)
        one.save()

    if Char.objects.filter(level=2):
        two = Char.objects.filter(level=2)[0]
    else:
        two = Char(level=2)
        two.save()

    if Char.objects.filter(level=3):
        three = Char.objects.filter(level=3)[0]
    else:
        three = Char(level=3)
        three.save()

    if Char.objects.filter(level=4):
        four = Char.objects.filter(level=4)[0]
    else:
        four = Char(level=4)
        four.save()

    if Char.objects.filter(level=5):
        five = Char.objects.filter(level=5)[0]
    else:
        five = Char(level=5)
        five.save()

    return render_to_response('index.html', locals())



def save(request):
    one_chars = request.REQUEST.get("one_chars")
    one = Char.objects.get(level=1)
    if one_chars:
        one.chars = one_chars
    one.save()

    two_chars = request.REQUEST.get("two_chars")
    two = Char.objects.get(level=2)
    if two_chars:
        two.chars = two_chars
    two.save()

    three_chars = request.REQUEST.get("three_chars")
    three = Char.objects.get(level=3)
    if three_chars:
        three.chars = three_chars
    three.save()

    four_chars = request.REQUEST.get("four_chars")
    four = Char.objects.get(level=4)
    if four_chars:
        four.chars = four_chars
    four.save()

    five_chars = request.REQUEST.get("five_chars")
    five = Char.objects.get(level=5)
    if five_chars:
        five.chars = five_chars
    five.save()

    return HttpResponseRedirect("/")


def view(request):
    article = request.REQUEST.get("article")
    one_chars = Char.objects.get(level=1).chars
    two_chars = Char.objects.get(level=2).chars
    three_chars = Char.objects.get(level=3).chars
    four_chars = Char.objects.get(level=4).chars
    five_chars = Char.objects.get(level=5).chars
    ones = []
    twos = []
    threes = []
    fours = []
    fives = []
    for char in article:
        if char in one_chars:
            ones.append([char, one_chars.find(char)+1])
        if char in two_chars:
            twos.append([char, two_chars.find(char)+1])
        if char in three_chars:
            threes.append([char, three_chars.find(char)+1])
        if char in four_chars:
            fours.append([char, four_chars.find(char)+1])
        if char in five_chars:
            fives.append([char, five_chars.find(char)+1])
    rs = [ones, twos, threes, fours, fives]
    return render_to_response('view.html', locals())

#====================login=============================================
def login(request):
    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
    return HttpResponseRedirect("/admin/")

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect("/admin/")
#======================================================================
