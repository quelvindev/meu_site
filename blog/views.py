from django.shortcuts import render
from django.http import HttpResponse
import requests
#from blog.data import posts

# Create your views here.

url = 'https://jsonplaceholder.typicode.com/posts'

posts = requests.get(url).json()

found_post = None



def blog(request):
    context ={
    'text':'Dados serão atualizados',
    'posts':posts
    }
    return render(request,'blog/blog.html',context)


def post(request,id):
    for post in posts:
        if post['id'] == id:
            found_post = post
            break

    context ={
    'text':'Dados serão atualizados',
    'post':found_post
    }
    
    print('chegou na view',found_post)
    return render(request,'blog/post.html',context)


def exemplo(request):
    return render(request,'blog/exemplo.html')