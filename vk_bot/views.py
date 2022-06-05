from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


async def index(request):
    return HttpResponse('Test')


async def confirm(request):
    if request.method == 'POST':
        print(request)
        return '986c9da8'
