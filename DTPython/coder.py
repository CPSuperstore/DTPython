import typing
from textwrap import wrap

CHAR_TO_BIN = b'0123456789,\n.-|\0'
STR_TO_BIN = CHAR_TO_BIN.decode("utf8")


def encode_message(message: typing.Union[str, bytes], encoding: str = "UTF-8") -> bytes:
    if isinstance(message, str):
        message = message.encode(encoding)

    # strip whitespace
    message = message.replace(b' ', b'')
    binary = []

    for char in message:
        binary.append(bin(CHAR_TO_BIN.index(char))[2:].zfill(4))

    if len(binary) % 2 == 1:
        binary.append("1111")

    return "".join(chr(int(''.join(x), 2)) for x in zip(binary[0::2], binary[1::2])).encode(encoding)


def decode_message(message: bytes) -> str:
    message = [wrap(bin(i)[2:].zfill(8), 4) for i in message]
    return ''.join(STR_TO_BIN[int(item, 2)] for sublist in message for item in sublist).strip("\0")
