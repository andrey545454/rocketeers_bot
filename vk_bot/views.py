from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import json


# Work with vk
from vk_bot.vk.vk_api import *

# Create your views here.


async def index(request):
    match request.method:
        case 'GET':
            return HttpResponse()
        case 'POST':
            data = json.loads(request.body)
            if data.get('secret') == VK_SECRET:
                match data.get('type'):
                    case MessageType.CONFIRMATION:
                        return HttpResponse(get_confirmation_code())
                    case MessageType.MESSAGE_NEW:
                        await parse_message_obj(data['object'])
                        return HttpResponse('ok')
                    case MessageType.MESSAGE_REPLY:
                        return HttpResponse('ok')
    return HttpResponseNotFound()


