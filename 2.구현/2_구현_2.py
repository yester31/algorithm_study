# 완전 탐색 문제

from random import randint

#h = randint(0, 23) # 0 <= N <=23
h = 5
result = 0
for i in range(h + 1) :
    for j in range(60):
        for k in range(60):
             if '3' in str(i) +str(j)+str(k):
                result+=1

print(h)
print(result)