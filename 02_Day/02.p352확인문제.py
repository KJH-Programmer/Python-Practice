#%%
# 1번
numbers = [1, 2, 3, 4, 5, 6]

# ## 반복문
# for i, number in enumerate(numbers):
#     numbers[i] = str(numbers)

## 고차함수
numbers = map(lambda x: str(x), numbers)
numbers = map(str, numbers)

# ## 리스트 컨프리헨션
# numbers = [str(number) for number in numbers]

print("::".join(numbers))
print()

#%% 2번
numbers = list(range(1, 10 + 1))
print("홀수만 추출하기")
print(list(filter(lambda x: x % 2 == 1, numbers)))
print()

print("# 3이상, 7 미만 추출")
print(list(filter(lambda x: x >= 3 and x < 7, numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x: x * x < 50, numbers)))
print()
# %%
