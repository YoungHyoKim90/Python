from random import random
import random

import numpy


lotto = []
rnd_num = random.randint(1, 45)

for i in range(6):
    while rnd_num in lotto:
        rnd_num = random.randint(1, 45)
    lotto.append(rnd_num)

lotto.sort()
print("로또번호: {}".format(lotto))


lotto2 = random.sample(range(1, 45), 6)
print("로또번호: {}".format(lotto2))