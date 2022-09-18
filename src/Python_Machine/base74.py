import math


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


def b74_encode(num: int) -> str:
    if num < 74:
        return str(b74_key[num % 74])

    output = ""
    while num > 0:
        output = b74_key[math.floor(num % 74)] + output
        num = math.floor(num / 74)

    return output
