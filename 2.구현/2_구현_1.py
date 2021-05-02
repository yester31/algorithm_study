import time
data = list(input().split())
n = len(data)

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

d = dict()
d['L'] = [-1, 0]
d['R'] = [1, 0]
d['U'] = [0, -1]
d['D'] = [0, 1]

x = 1
y = 1
for i in data :
    if x + d[i][0] == 0 or y + d[i][1] == 0 :
        continue
    else :
        x += d[i][0]
        y += d[i][1]

end_time = time.time() # 측정 종료
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time) # 수행 시간 출력
print(x,y)

