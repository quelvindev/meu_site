from django.shortcuts import render
from django.http import HttpResponse
from blog.data import posts

# Create your views here.

context ={
    'text':'Dados serão atualizados',
    'posts':posts
}

def blog(request):
    print('chegou na view')
    return render(request,'blog/blog.html',context)


def exemplo(request):
    return render(request,'blog/exemplo.html')