import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.isqrt(n)
    for d in range(3, max_divisor + 1, 2):
        if n % d == 0:
            return False
    return True