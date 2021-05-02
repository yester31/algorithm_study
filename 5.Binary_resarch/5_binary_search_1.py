# 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정 합니다.

# 이진 탐색 소스코드 구현( 재귀 함수 )
def binary_search(array, target, start, end) :
    if start > end:
        return None
    mid = (start + end) // 2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

def binary_search2(array, target, start, end) :
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None



target = 7
array = [1,3,5,7,9,11,13,15,17,19]

result = binary_search2(array, target, 0, len(array)-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else :
    print(result+1)