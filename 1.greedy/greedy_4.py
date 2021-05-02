import time

n, k = map(int, input().split())

start = time.time()
result = 0
while True:
    target = (n//k)*k
    result += (n - target)
    n = target

    if n < k :
        break

    result +=1
    n//=k

result += (n-1)
dur_tiem = time.time() - start
print(dur_tiem)
print(result)

