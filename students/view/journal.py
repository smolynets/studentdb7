# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
def vid(request):
    return render(request, 'students/vid.html', {})
