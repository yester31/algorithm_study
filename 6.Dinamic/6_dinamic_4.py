x = int(input())
d= [0] * 30001
# a_i = i 를 1로 만들기 위한 최소 연산 횟수
# 점화식 = a_i = min(a_i-1, a_i/2, a_i/3, a_i/5) + 1
for i in range(2, x+1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2]+1)

    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3]+1)

    if i % 5 == 0 :
        d[i] = min(d[i], d[i//5]+1)

print(d[x])