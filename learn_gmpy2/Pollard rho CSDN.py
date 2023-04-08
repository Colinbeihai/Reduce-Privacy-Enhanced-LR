'''
来源：CSDN，https://blog.csdn.net/TH_NUM/article/details/51477719

Pollard rho方法是一种随机算法，用于解决大整数因数分解问题。
该算法由约翰·波拉德（John Pollard）在1975年提出，它是一种Monte Carlo算法，因此其运行时间是随机的。

Pollard rho方法的核心思想是利用随机游走的方式来找到大整数的一个因子。
具体来说，该算法从一个随机数开始，重复进行下列操作：

1. 计算函数f(x)，f(x)是待分解整数的一个函数，通常是形如f(x) = x^2 + a mod n的多项式函数。
2. 根据f(x)计算出一个新的随机数y。
3. 计算gcd(|x - y|, n)，如果gcd不等于1或n，则x和y的差即为待分解整数n的一个因子。

'''

import gmpy2 as gp
import time
start = time.perf_counter()

n = gp.mpz(63281217910257742583918406571)
x = gp.mpz(2)
y = x**2 + 1
for i in range(n):
    p = gp.gcd(y-x, n)
    if p != 1:
        print(p)
        break
    else:
        y = (((y**2+1)%n)**2+1)%n
        x = (x**2+1)%n
end = time.perf_counter()
print(end - start)
