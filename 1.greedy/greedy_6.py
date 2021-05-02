
data = list(map(int, input().split()))
n = len(data)
data.sort() # 오름차순 정렬

result = 0              # 총 그룹의 수
count = 0               # 현재 그룹에 포함된 모험가의 수

for i in data:          # 공포도를 낮은 것 부터 하나씩 확인하며
    count += 1          # 현재 그룹에 해당 모험가를 포함 시키기
    if count >= i :     # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1     # 총 그룹의 수 증가 시키기
        count = 0       # 현재 그룹에 포함된 모험가의 수 초기화

print(result)           # 총 그룹의 수 출력


