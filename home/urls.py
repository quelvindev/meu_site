

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse



def home(reponse):
    return HttpResponse('Pagina inicial Django')