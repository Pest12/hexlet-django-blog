from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    tags = ['article']
    return render(
        request,
        'articles/index.html',
        context={'tags': tags},
    )
