def is_prime(n):
    if n < 2: return False

    for k in range(2, int(n ** (1/2)) + 1):
        if n % k == 0:
            return False

    return True

