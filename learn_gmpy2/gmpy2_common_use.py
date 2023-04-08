import gmpy2
import math
import time

a = gmpy2.gcd(3, 12)
print('a,b的最大公因数是{}'.format(a))

a = gmpy2.is_prime(5)
print('a为5是否为素数的结果{}'.format(a))

a = gmpy2.is_even(4)
b = gmpy2.is_odd(4)
print('a为4是否为偶数的结果{}'.format(a))
print('b为4是否为奇数的结果{}'.format(b))

num1 = 16
num2 = 2
a = gmpy2.iroot(num1, num2)
print('对{}开{}次方的结果是{}'.format(num1, num2, a))
a0 = a[0]
print('a0的值是{}'.format(a0))

num3 = 5678987656789
a = gmpy2.mpz(num3)
print('初始化大整数后a为{}'.format(a))
print('a的数据类型是{}'.format(type(a)))
c = math.ceil(math.log(num3, 2))    #向上取整
print('{}的比特数是{}'.format(num3, c))
print('\nnum3是否是素数{}\n'.format(gmpy2.is_prime(num3)))

a = gmpy2.invert(3, 13)
print('invert是一个求数模x的逆元函数，上式结果为{}'.format(a))

num1 = 3
num2 = 4
num3 = 4
a = gmpy2.powmod(num1, num2, num3)
print('{}的{}次方模{}的余数是{}'.format(num1, num2, num3, a))

a = gmpy2.mpz(91)
b = a/3
print('a/3之后的类型为{}，值为{}'.format(type(b), b))
c = a//3
print('a//3之后的类型为{}，值为{}'.format(type(c), c))

'''
start2 = time.perf_counter()
b = gmpy2.mpz(1257787) ** 12345678
end2 = time.perf_counter()
time2 = end2 - start2
# print('结果是{}，耗时{}'.format(b, end2 - start2))
print('使用gmpy2库的mpz类型计算所画时间{}'.format(time2))

start1 = time.perf_counter()
a = 1257787 ** 12345678
end1 = time.perf_counter()
time1 = (end1 - start1)
# print('结果是{}，耗时{}'.format(a, end1 - start1))
print('python直接计算所花时间{}'.format(time1))
print('两种算法结果是否相等{}'.format(a == b))
'''

a = gmpy2.next_prime(9789678909876567890987656789)
print('next_prime的用法，a的值是{}'.format(a))