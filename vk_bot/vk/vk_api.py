import aiohttp
import json
import logging

from decouple import config
from enum import Enum

from .utils import *


logger = logging.getLogger(__name__)


VK_API_TOKEN = config('VK_API_TOKEN')
VK_API_V = config('VK_API_V')
VK_CONFIRM_CODE = config('VK_CONFIRM_CODE')
VK_SECRET = config('VK_SECRET')


class MessageType(str, Enum):
    """ List of messsages from API """

    CONFIRMATION = 'confirmation'
    MESSAGE_NEW = 'message_new'
    MESSAGE_REPLY = 'message_reply'


class CommandType(str, Enum):
    """ List of commands """
    START = 'start'


class ButtonType(str, Enum):
    """ List of platforms """

    STEAM = 'steam'
    EPIC = 'epic'
    PLAYSTATION = 'psn'
    XBOX = 'xbl'


class Keyboards:
    """ List of keyboards """

    PLATFORM_KEYBOARD = json.dumps({
        'one_time': False,
        'buttons': [[
            {'action': {
                'type': 'text',
                'payload': f'{{"command": "{button.value}"}}',
                'label': button.name
            }}
            for button in ButtonType
        ]]
    })


async def parse_message_obj(obj: dict):
    msg = obj['message']
    msg_text = msg['text']
    from_id = msg['from_id']
    payload = json.loads(msg['payload'])
    print(Keyboards.PLATFORM_KEYBOARD)
    match payload.get('command'):
        case CommandType.START:
            await vk_send_message(
                from_id,
                'Здравствуйте! Чтобы добавить себя выберите платформу',
                Keyboards.PLATFORM_KEYBOARD
            )
        case _:
            await vk_send_message(from_id, 'Ошибка! Повторите процесс заного')


async def vk_send_message(to_id: int, msg: str, keyboard: dict = None, payload: str = ''):

    async with aiohttp.request(
        'POST',
        'https://api.vk.com/method/messages.send',
        params={
            'access_token': VK_API_TOKEN,
            'user_id': to_id,
            'random_id': get_random_id(),
            'message': msg,
            'keyboard': keyboard,
            'payload': payload,
            'v': VK_API_V}
    ) as resp:

        logger.info(f'Send message to {to_id} - response [{resp.status}]')
        logger.info(f'{await resp.json()}')
