from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    print('chegou na view')
    return render(request,'blog/blog.html')


def exemplo(request):
    return render(request,'blog/exemplo.html')