from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .init_data import init_workers, init_cases


def home(request):
    context = {'employees': init_workers(),
               'cases': init_cases()}
    return render(request, 'main/home.html', context)


def about(request):
    context = {'employees': init_workers()}
    return render(request, 'about/main.html', context)


def about_workers(request):
    context = {'employees': init_workers()}
    return render(request, 'about/workers.html', context)


def about_workers_id(request, employee_id):
    employee = init_workers()
    for i in employee:
        if i['user_id'] == employee_id:
            employee = i
            break
    context = {'employee': employee}
    return render(request, 'about/employees/base.html', context)


def about_cases(request):
    context = {'cases': init_cases()}
    return render(request, 'about/case.html', context)



