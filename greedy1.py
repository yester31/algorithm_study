# 그리디 알고리즘 2

# n, m, k, 입력 받기  (예시 입력 : 5 8 3)
n,m,k = map(int,input().split())
# n 개의 수 입력받기   (입력 예시 : 2 4 5 4 6)
data = list(map(int, input().split()))

data.sort() # 입력 받은 수 정렬하기
first = data[n-1] # 가장 큰수
second = data[n-2] # 두번째 큰수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)



