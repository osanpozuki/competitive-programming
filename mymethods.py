def is_prime(n):
    if n < 2: return False

    for k in range(2, int(n ** (1/2)) + 1):
        if n % k == 0:
            return False

    return True


# using: 1 2 3 => [1, 2, 3]
def input_parse_int():
    return [int(i) for i in input().split(' ')]
