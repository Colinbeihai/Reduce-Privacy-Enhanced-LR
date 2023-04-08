import random
import gmpy2
import math

def generate_keypair(bit_length):
    # 生成公钥和私钥
    p = gmpy2.next_prime(random.getrandbits(bit_length)) #next_prime()总是返回该数的下一个素数
    q = gmpy2.next_prime(random.getrandbits(bit_length))
    p = 17
    q = 5
    n = p * q
    lambda_n = gmpy2.lcm(p-1, q-1)
    g = n + 1
    mu = gmpy2.invert(lambda_n, n)
    return (n, g), (lambda_n, mu)

def encrypt(m, public_key):
    # 加密明文
    n, g = public_key
    r = gmpy2.mpz_random(gmpy2.random_state(), n)
    c = (pow(g, m, n*n) * pow(r, n, n*n)) % (n*n)
    return c

def decrypt(c, private_key, public_key):
    # 解密密文
    lambda_n, mu = private_key
    n, g = public_key
    u = pow(c, lambda_n, n*n) - 1
    m = ((u // n) * mu) % n  # //表示地板除
    return m

# 测试代码
bit_length = 128
public_key, private_key = generate_keypair(bit_length)
m = gmpy2.mpz( 26 )
c = encrypt(m, public_key)
decrypted_m = decrypt(c, private_key, public_key)
print("明文: {}".format(m))
print("密文: {}".format(c))
print("解密后的明文: {}".format(decrypted_m))
