# arr = input()
# print(arr, type(arr))

# # 입력값 2143 이 str 이다

# 방법1
arr = sorted(input(), reverse=True)
for element in arr:
    print(element, end='')

# 방법2
arr = ''.join(sorted(input(), reverse=True))
print(arr)

