# 첫줄에 자연수 추력, 두번째줄에 약수의 개수 출력
s = "g0en2Ts8eSoft"

res = 0
for x in s:
    if x.isdecimal(): # 0 ~ 9 까지 숫자면 True 반환
        res = res * 10 + int(x)
print(res)

# 약수의 개수 계산
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)