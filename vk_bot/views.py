from django.shortcuts import render
from django.http import HttpResponse, Http404


# Work with vk
from vk_bot.vk.vk_api import *

# Create your views here.


async def index(request):
    if request.method == 'POST':
        match request.POST['type']:
            case MessageType.CONFIRM:
                return HttpResponse(confirmation())
            case _:
                return Http404()
    else:
        return HttpResponse('Test')

