import shara

N = int(input("Введите модуль(должен быть нечетным): "))
T = int(input("Введите приводимое число: "))
b = len(shara.to_bin(N))
R = 1 << b
gcd = shara.gen_gcd(R, N)
while gcd[0] != 1:
    print("Алгоритм дальше работать не будет")
    break
while T >= R * N or shara.inverse(R, N) != 1:
    R <<= 1
    b += 1
N1 = (shara.inverse(N, R)*((-1) % R)) % R
'''
R1, N1 = gcd[1], gcd[2]
print('R * R1 - N * N1 = 1')
print(str(R) + ' * ' + str(R1) + ' - ' + str(N) + ' * ' + str(N1) + ' = 1')
'''
m = T % R
m = (m * N1) % R
tx = (T + m * N) >> b
if tx >= N:
    assert(T % N == tx - N)
    print('Наименьший неотрицательный вычет: ' + str(tx - N))
else:
    assert (T % N == tx)
    print('Наименьший неотрицательный вычет: ' + str(tx))