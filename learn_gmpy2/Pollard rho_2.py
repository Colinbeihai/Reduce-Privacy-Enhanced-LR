'''
来源：ChatGPT
原方法使用了random和math库，这里使用gmpy2进行改写
作者：ZhaoChen
'''

import gmpy2 as gp
import random
import math

import random
from math import gcd
import time

'''
def pollard_rho(n):
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)

    return d
'''

def pollard_rho(n):
    x = gp.mpz(random.randint(2, n-1))
    y = x
    c = gp.mpz(random.randint(1, n-1))
    d = 1

    while d == 1:
        x = (x*x + c) % n
        y = (y*y + c) % n
        y = (y*y + c) % n
        d = math.gcd(abs(x-y), n)
        if d == n:
            return pollard_rho(n)

    return d

start = time.perf_counter()
n = 63281217910257742583918406571
ans = pollard_rho(n)
end = time.perf_counter()
print('结果是{}，耗时{}'.format(ans, end-start))

