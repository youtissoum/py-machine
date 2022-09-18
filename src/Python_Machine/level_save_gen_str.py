from .base74 import b74_encode

def case_one(maxMatchOffset, maxMatchLength):
    return f"){b74_encode(maxMatchOffset)}{b74_encode(maxMatchLength)}"

def case_two(maxMatchOffset, maxMatchLength):
    return f"({b74_encode(maxMatchOffset)}){b74_encode(maxMatchLength)}"

def case_three(maxMatchOffset, maxMatchLength):
    return f"({b74_encode(maxMatchOffset)}({b74_encode(maxMatchLength)})"