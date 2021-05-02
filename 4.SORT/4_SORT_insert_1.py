array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    min_index = i               # 가장 작은 원소의 인덱스
    for j in range(i, 0, -1):   # i부터 0까지 -1 step 씩
        if array[j] < array[j-1]:
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp
        else:                   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
