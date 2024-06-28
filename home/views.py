
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

context ={
    'text':'Dados serão atualizados',
    'title':'Home'
}

def home(request):
    print('chegou na view')
    return render(request,
                  'home/home.html',
                  context
                  )


