import shara

if __name__ == '__main__':
    k = int(input("Введите количество уравнений системы: "))
    a = []
    m = []
    print("Введите а-итые и m-итые парами:")
    for i in range(0, k):
        am = input().split()
        a.append(int(am[0]))
        m.append(int(am[1]))

    x = []
    for i in range(k):
        x.append(a[i])
        for j in range(i):
            x[i] = (shara.inverse(m[j], m[i]) * (x[i] - x[j])) % m[i]

    xx = x[0]
    for i in range(1, k):
        mm = x[i]
        for j in range(0, i):
            mm *= m[j]
        xx += mm
    print("Решение системы = " + str(xx))