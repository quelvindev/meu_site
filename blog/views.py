from django.shortcuts import render
from django.http import HttpResponse
import requests
#from blog.data import posts

# Create your views here.

url = 'https://jsonplaceholder.typicode.com/posts'

posts = requests.get(url).json()


context ={
    'text':'Dados serão atualizados',
    'posts':posts
}

def blog(request):
    print(type(context))

  
    return render(request,'blog/blog.html',context)


def post(request,id):
    context['page'] = 'post'
    print('chegou na view',id)
    return render(request,'blog/blog.html',context)


def exemplo(request):
    return render(request,'blog/exemplo.html')