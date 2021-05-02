# a_i = i번째 식량창고까지의 최적의 해(얻을 수 있는 식량의 최대값)
# k_i = i번째 식량창고에 있는 식량의 양
# a_i = max(a_i-1, a_i-2 + k_i)
array = [1, 3, 1, 5]
n = len(array)
d = [0] * 100 # 앞서 계산된 결과를 저장하기 위한 dp 테이블 초기화 
# 다이나믹 프로그래밍 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])

