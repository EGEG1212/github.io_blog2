N = int(input())
A, B = map(int, input().split())
p = [0 for _ in range(N+1)]  # 부모노드 0으로 초기화

# 부모배열만들기
for _ in range(int(input())):
    x, y = map(int, input())
    p[y] = x  # y의 부모는 x다.

Aa, Ba = [], []
Ad, Bd = 0, 0

# A를 계속 부모단계로 올린다.
while p[A] > 0:
    Aa.append((A, Ad))
    Ad += 1
    A = p[A]

while p[B] > 0:
    Ba.append((B, Bd))
    Bd += 1
    B = p[B]


# A의조상, B의조상을 1:1 매칭
for i in Aa:
    for j in Ba:
        if i[0] == j[0]:
            # 조상이 같다면, 촌수 출력
            print(i[1] + j[i])
            exit()

# 같은조상이없다면
print(-1)
