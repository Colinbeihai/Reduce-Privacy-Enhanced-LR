import random
import math
import gmpy2 as gp


def _random(bits, maximum):
    rand_function = random.SystemRandom()
    r = gp.mpz(rand_function.getrandbits(bits))
    while r >= maximum:
        r = gp.mpz(rand_function.getrandbits(bits))
    return r


def _random_prime(bits):
    rand_function = random.SystemRandom()
    a = gp.mpz(rand_function.getrandbits(bits))
    while True:
        if gp.is_prime(a):
            break
        else:
            a = gp.mpz(rand_function.getrandbits(bits))
    return a


def _param_generator(bits):
    p = _random_prime(bits)  # 安全参数取1024时，令p和q相差8比特左右
    while True:
        if gp.is_prime(gp.mpz((p - 1) / 2)):
            break
        else:
            p = _random_prime(bits)
    return p


def _random_generator(N):
    while True:
        a = random.randint(1, (N ** 2) - 1)
        if gp.gcd(a, N ** 2) == 1:
            g = gp.powmod(a, 2 * N, N ** 2)
            if not g == 1:
                break
    return g


# 随机生成一个安全素数
def safeprimeGen(bits):
    p_floor = 2 ** (bits - 1)
    p_ceiling = 2 ** bits
    while True:
        p = random.randint(p_floor, p_ceiling)
        # (p - 1)/2也是素数，确保p为安全素数
        if gp.is_prime(p) and gp.is_prime(p >> 1):
            break
    return p


