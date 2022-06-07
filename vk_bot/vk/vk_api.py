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


class CommandType(str, Enum):
    """ List of commands """
    START = 'start'


class VkKeyboardColor(Enum):
    """ List of colors """

    # Blue
    PRIMARY = 'primary'

    # White
    SECONDARY = 'secondary'

    # Red
    NEGATIVE = 'negative'

    # Green
    POSITIVE = 'positive'


class ButtonType(str, Enum):
    """ List of platforms """

    PLAYSTATION = 'psn'
    XBOX = 'xbl'
    STEAM = 'steam'
    EPIC_GAMES = 'epic'


def get_confirmation_code() -> str:
    return VK_CONFIRM_CODE


async def parse_message_obj(obj: dict):
    msg = obj['message']
    msg_text = msg['text']
    user_id = msg['from_id']
    await send_message(user_id, msg_text)


async def send_message(to_id: int, msg: str):
    cl_msg = clean_message(msg)
    answer_msg = ''
    match cl_msg:
        case CommandType.START:
            answer_msg = 'Здравствуйте! Чтобы добавить себя выберите платформу'

    if answer_msg:
        await vk_send_message(to_id, answer_msg)


async def vk_send_message(to_id: int, msg: str):

    async with aiohttp.request(
        'POST',
        'https://api.vk.com/method/messages.send',
        params={
            'access_token': VK_API_TOKEN,
            'user_id': to_id,
            'random_id': get_random_id(),
            'message': msg,
            'v': VK_API_V}
    ) as resp:

        logger.info(f'Send message to {to_id} - response [{resp.status}]')
