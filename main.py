import math

def read_int() -> int:
    try:
        return int(input())
    except ValueError:
        raise ValueError("Wprowadzona wartość musi być liczbą całkowitą")

def prime_factors(n: int) -> list[int]:
    if n < 2:
        return []
    factors: list[int] = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

def print_factors(factors: list[int]) -> None:
    for f in factors:
        print(f)

if name == "main":
    print_factors(prime_factors(read_int()))