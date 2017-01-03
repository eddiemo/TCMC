import shara
import math

def gauss(a, b):
    n = int(len(a))
    row = 0
    while row < n:
        sel = row
        for i in range(row + 1, n):
            if abs(a[i][row]) > abs(a[sel][row]):
                sel = i
        a[row], a[sel] = a[sel], a[row]
        b[row], b[sel] = b[sel], b[row]
        for i in range(row + 1, n):
            a[row][i] /= a[row][row]
        b[row] /= a[row][row]
        for i in range(n):
            if i != row and a[i][row] != 0:
                for j in range(row + 1, n):
                    a[i][j] -= a[row][j] * a[i][row]
                b[i] -= b[row] * a[i][row]
        row += 1
    for i in range(len(b)):
        if abs(b[i]) - int(abs(b[i])) > 0.999:
            if b[i] > 0:
                b[i] = int(b[i]) + 1
            else:
                b[i] = int(b[i]) - 1
        else:
            b[i] = int(b[i])
    return b

a = []
b = []
f = open('example.txt', 'r')
for line in f:
    x = []
    for i in range(len(line.split()) - 1):
        x.append(int(line.split()[i]))
    a.append(x)
    b.append(int(line.split()[-1]))
ans = gauss(a, b)
print(ans)