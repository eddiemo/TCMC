def solution(a, b):
    eps = 0.001
    n = len(a)
    ans = [0] * n
    while True:
        curans = [0] * n
        for i in range(n):
            curans[i] = b[i]
            for j in range(n):
                if i != j:
                    curans[i] -= a[i][j] * ans[j]
            curans[i] /= a[i][i]
        error = 0
        for i in range(n):
            error += abs(curans[i] - ans[i])
        if error < eps:
            break
        ans = curans
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