import pytest
from prime_checker import is_prime

def test_is_prime():
    # Test non-prime and edge cases
    assert not is_prime(-1)  # Negative input (handled by ValueError)
    assert not is_prime(0)   # Zero
    assert not is_prime(1)   # 1 is not prime
    assert not is_prime(4)   # Small even composite
    assert not is_prime(9)   # Composite square of prime (3*3)
    assert not is_prime(15)  # Odd composite
    
    # Test primes
    assert is_prime(2)       # Smallest prime
    assert is_prime(3)       # Small odd prime
    assert is_prime(17)      # Larger prime
    assert is_prime(7919)    # Known large prime (1000th prime)

def test_type_errors():
    with pytest.raises(TypeError):
        is_prime("hello")    # String input
    with pytest.raises(TypeError):
        is_prime(5.5)        # Float input

def test_value_errors():
    with pytest.raises(ValueError):
        is_prime(-10)        # Negative integer