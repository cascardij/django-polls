from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#View Index
def index(request):
    return HttpResponse("Olá, seja bem vindo a enquete")