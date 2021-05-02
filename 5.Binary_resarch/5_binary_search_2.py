from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value) # 정렬 되어 있는 리스트에 대하여 right_value값이 순서에 맞게 들어갈 인덱스(중복값이 있으면 그 값의 오른쪽 끝)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))