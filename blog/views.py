from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    print('chegou na view')
    return HttpResponse('Teste blog')



def exemplo(request):
    return HttpResponse('Teste exemplo')