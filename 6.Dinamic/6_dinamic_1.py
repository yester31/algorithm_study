
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        first = 1
        seconde = 1
        target = 0
        for _ in range(n-2):
            target = first + seconde
            first = seconde
            seconde = target
        return target

def fibo1(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo1(7))

# 한번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100

def fibo2(x):
    if x == 1 or x == 2: # 종료 조건
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo2(99))


