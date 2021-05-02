import sys
#sys.stdin = open("input.txt", "rt")
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
n, k = 10, 3
a = [13,15,34,23,45,65,33,11,26,42]
res = set() # 중복값 제거시 사용

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])# 중복을 제거하면서 합 저장

res = list(res) # set 을 list 변환
res.sort(reverse=True)# 내림차순으로 정렬
print(res[k-1])


