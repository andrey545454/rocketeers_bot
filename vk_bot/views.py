from django.shortcuts import render

# Work with vk
from vk_bot.vk.vk_api import *

# Create your views here.


async def index(request):
    if request.method == 'POST':
        match request.POST['type']:
            case MessageType.CONFIRM:
                return confirmation()
            case '':
                pass
    else:
        return HttpResponse('Test')

