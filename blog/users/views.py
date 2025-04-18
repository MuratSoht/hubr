from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return HttpResponse('Страница аутентификации')

def registr(request):
    return HttpResponse('Страница регистрации')

def get_personal_account(request):
    return HttpResponse('Страница личного кабинета пользователя')