import shara
import math

def solution(a, b):
    n = len(a[0])
    x = [0] * n
    y = [0] * n
    z = [0] * n
    y[0], z[0] = a[0][0], a[0][1]
    x[n-1], y[n-1] = a[n - 1][n - 2], a[n - 1][n - 1]
    for i in range(1, n - 1):
        x[i] = a[i][i - 1]
        y[i] = a[i][i]
        z[i] = a[i][i + 1]
    for i in range(1, n):
        m = x[i] / y[i - 1]
        y[i] = y[i] - m * z[i - 1]
        b[i] = b[i] - m * b[i - 1]
    ans = [0] * n
    ans[n - 1] = b[n - 1] // y[n - 1]
    for i in range(n - 2, -1, -1):
        ans[i] = (b[i] - z[i] * ans[i+1]) // y[i]
    return ans

a = []
b = []
f = open('example.txt', 'r')
for line in f:
    x = []
    for i in range(len(line.split()) - 1):
        x.append(int(line.split()[i]))
    a.append(x)
    b.append(int(line.split()[-1]))
ans = solution(a, b)
print(ans)