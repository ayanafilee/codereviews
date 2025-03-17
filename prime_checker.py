import math

def is_prime(n: int) -> bool:
    """
    Determines if a positive integer is a prime number.
    
    Args:
        n (int): The integer to check for primality.
        
    Returns:
        bool: True if `n` is prime, False otherwise.
        
    Raises:
        TypeError: If `n` is not an integer.
        ValueError: If `n` is negative.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    max_divisor = math.isqrt(n)  # Efficient square root calculation
    for d in range(3, max_divisor + 1, 2):
        if n % d == 0:
            return False
    return True