from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import json


# Work with vk
from vk_bot.vk.vk_api import *

# Create your views here.


async def index(request):
    match request.method:
        case 'GET':
            return HttpResponse('Test')
        case 'POST':
            data = json.loads(request.body)
            match data['type']:
                case MessageType.CONFIRMATION:
                    return HttpResponse(get_confirmation_code())
                case _:
                    return HttpResponseNotFound()


