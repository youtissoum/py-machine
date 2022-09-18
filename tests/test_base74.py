from Python_Machine.base74 import b74_decode, b74_encode
import pytest

def test_b74_decode():
    assert b74_decode("1q") == 100, "did not decode correctly"
    with pytest.raises(ValueError):
        b74_decode("\x00")

def test_b74_encode():
    assert b74_encode(100) == "1q"
    assert b74_encode(5) == "5"