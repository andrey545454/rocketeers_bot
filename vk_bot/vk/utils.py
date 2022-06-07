from random import getrandbits


def clean_message(msg: str) -> str:
    cl_msg = msg.strip().lower()
    return cl_msg


def get_random_id() -> int:
    return getrandbits(31)
