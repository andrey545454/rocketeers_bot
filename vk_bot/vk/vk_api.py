from django.http import HttpResponse
from enum import Enum

VK_CONFIRM_CODE = '986c9da8'


class MessageType(Enum):
    CONFIRM = 'confirm'


def confirmation():
    return HttpResponse(VK_CONFIRM_CODE)
