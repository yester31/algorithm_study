
data = list(map(int, input().split()))

result = data[0]
for i in range(1, len(data)):
    num = data[i]
    if num <= 1 or result <=1:
        result += num
    else :
        result *= num

print(data)
print(result)


