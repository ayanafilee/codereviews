import pytest
from prime_checker import is_prime

def test_is_prime():
    assert not is_prime(-1)
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(17)
    assert is_prime(7919)