import random
import gmpy2 as gp

p = 7
q = 11
m = 8
r = random.randint(14, 16)
print('随机出r的值为{}'.format(r))

N = p * q
lamb = gp.lcm(p-1, q-1)
g = random.randint(6, 8)
mid = gp.gcd((g**lamb)%(N**2), N)
while mid != 1:
    g = random.randint(6, 8)
    mid = gp.gcd((g ** lamb) % (N ** 2), N)
C = (g**m * r**N)%(N**2)

#接收方使用私钥(p, q, lamb)进行解密

x = (((C**lamb % N**2)-1)/N) % N
L = (((g**lamb % N**2)**(lamb-1))/ N)% N
miu = (L(g**lamb % N**2))**(-1) % N
m_de = L(C**lamb % N**2) * miu % N
print('解密出来的m是{}'.format(m))


'''
class Paillier(object):
    pass

    def setup(self):
        pass
'''