array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array)+1)    # array 원소의 값중 최대값을 선택하고 0을 포함하기 위해 1을 더한 개수 만큼 리스트 선언

for i in range(len(array)):
    count[array[i]] += 1        # 각 데이터에 해당하는 인덱스의 값 증가

for i  in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')       # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력