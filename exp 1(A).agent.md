def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Find and print all twin primes where both numbers are < 1000
for p in range(2, 998):
    if is_prime(p) and is_prime(p + 2):
        print(f"({p}, {p + 2})")