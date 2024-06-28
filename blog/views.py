from django.shortcuts import render
from django.http import HttpRequest,Http404
from typing import Any

import requests
#from blog.data import posts

# Create your views here.

url = 'https://jsonplaceholder.typicode.com/posts'

posts = requests.get(url).json()





def blog(request):
    context ={
    'text':'',
    'posts':posts,
    'title':'Blog'
    }
    return render(request,'blog/blog.html',context)


def post(request: HttpRequest,id: int):
    found_post: dict[str,Any] | None = None
    for post in posts:
        if post['id'] == id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe')
    
    context ={
    'text':'Dados serão atualizados',
    'post':found_post,
    
    }
    
    print('chegou na view',found_post)
    return render(request,'blog/post.html',context)


def exemplo(request):
    context = {
        'title':'Exemplo'   
    }
    return render(request,'blog/exemplo.html',context)