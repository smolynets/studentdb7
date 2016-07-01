# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from ..models.group import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def grup(request):
   groups = Group.objects.all()
   # try to order grup list
   order_by = request.GET.get('order_by', '')
   if order_by in ('group', 'leader', '#'):
     groups = groups.order_by(order_by)
     if request.GET.get('reverse', '') == '1':
       groups = groups.reverse()
   # paginate groups
   paginator = Paginator(groups, 3)
   page = request.GET.get('page')
   try:
     groups = paginator.page(page)
   except PageNotAnInteger:
   # If page is not an integer, deliver first page.
     groups = paginator.page(1)
   except EmptyPage:
     # If page is out of range (e.g. 9999), deliver
     # last page of results.
     groups = paginator.page(paginator.num_pages)
   return render(request, 'students/grup.html',
{'groups': groups})
def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)
def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
