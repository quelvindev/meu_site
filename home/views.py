
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    print('chegou na view')
    return render(request,
                  'home/home.html')


