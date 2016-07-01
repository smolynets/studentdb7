# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from ..models.student import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def students_list(request):
   students = Student.objects.all()
   # try to order students list
   order_by = request.GET.get('order_by', '')
   if order_by in ('last_name', 'first_name', 'ticket', '#'):
     students = students.order_by(order_by)
     if request.GET.get('reverse', '') == '1':
       students = students.reverse()
   # paginate students
   paginator = Paginator(students, 2)
   page = request.GET.get('page')
   try:
     students = paginator.page(page)
   except PageNotAnInteger:
   # If page is not an integer, deliver first page.
     students = paginator.page(1)
   except EmptyPage:
     # If page is out of range (e.g. 9999), deliver
     # last page of results.
     students = paginator.page(paginator.num_pages)
   return render(request, 'students/stud.html',
{'students': students})
def stud_add(request):
    return render(request, 'students/stud_add_form.html', {})
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
