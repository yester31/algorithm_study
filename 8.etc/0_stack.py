stack = []

stack.append(5)
print(stack)        # 최하단 부터 출력
stack.append(2)
print(stack)        # 최하단 부터 출력
stack.append(3)
print(stack)        # 최하단 부터 출력
stack.append(7)
print(stack)        # 최하단 부터 출력
stack.pop()
print(stack)        # 최하단 부터 출력
stack.append(1)
print(stack)        # 최하단 부터 출력
stack.append(4)
print(stack)        # 최하단 부터 출력
stack.pop()
print(stack)        # 최하단 부터 출력
print(stack[::-1])  # 최상단 부터 출력
