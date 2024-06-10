stack = []

# push 연산 (데이터 추가)
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)
print()

# pop 연산 - 가장 뒤에 있는 원소 삭제
top_element = stack.pop()
print(stack, top_element)
print()

# peek 연산 - 가장 위에 있는 원소 조회, 원소 삭제는 하지 않음
top_element = stack[-1]
print(stack, top_element)
print()

# is_empty 연산
is_empty = len(stack) == 0
print(is_empty)