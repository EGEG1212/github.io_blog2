N = int(input())
A, B = map(int, input().split())
p = [0 for _ in range(N+1)]

for _ in range(int(input())):
    x, y = map(int, input())
    p[y] = xrange

Aa, Ba = [], [0]
Ad, Bd = 0, 0

while a[A] > 0:
    Aa.append((A, Ad))
    Ad += 1
    A = p[A]

while p[B] > 0:
    Ba.append((B, Bd))
    Bd += 1
    B = p[B]

for i in Aa:
    for j in Ba:
        if i[0] == j[0]:
            print(i[1] + j[i])
            exit()

print(-1)
