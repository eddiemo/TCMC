import shara
import math

def dividers(n):
    z = int(math.sqrt(n))
    z = int(math.sqrt(n)) + 1
    t = n
    jj = 1
    for j in range(1, z + 1):
        jf = 1
        jz = j * z
        for k in range ((j - 1) * z + 1, jz + 1):
            jf = jf * k
        if shara.gen_gcd(jf, t)[0] != 0:
            jj = j
            break
    minDivider = 1
    for i in range((jj - 1) * z + 1, jj * z + 1):
        if t % i == 0 and i != 1:
            minDivider = i
            break
    return minDivider, n//minDivider

n = int(input('Введите n: '))
res = dividers(n)
assert res[0]*res[1] == n
print(res)