import random
import math

bit_length = 3
num = random.getrandbits(bit_length)    #生成不高于指定数的整数
if num != 0:
    bit = math.log(num, 2)
else:
    bit = 0
print('随机生成的数是{}，比特为{}'.format(num, bit))

a = random.SystemRandom.getrandbits(3, 5)
print('a的值是{}'.format(a))
