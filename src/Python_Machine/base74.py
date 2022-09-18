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


def b74_encode(input: int) -> str:
    result = ""

    if input < 74:
        return b74_key[round(input % 74)]

    while input > 0:
        result = f"{b74_key[round(input % 74)]}{result}"
        input = round(input / 74)

    return result
