b74_key = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&+-.=?^{}"

def b74_decode(chars: str, /) -> int:
    result = 0

    for char in chars:
        result *= 74
        if (b74_char := b74_key.find(char)) == -1:
            raise ValueError(f"Invalid character in base 74 number: {char}")
        else:
            result += b74_char

    return result

import base64
import math
def b74_encode(input: int) -> str:
    result = ""

    while input > 0:
        if input > 74:
            result = result + b74_key[math.floor(input/len(b74_key))]
            input -= math.floor(input/len(b74_key))*len(b74_key)
        else:
            result = result + b74_key[input]
            input = 0

    return result