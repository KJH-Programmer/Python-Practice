#%%
data = [64, 34, 25, 12, 22, 11, 90]

## 기본 정렬 (오름차순) - sorted()
sorted_data = sorted(data)
print("오름차순 정렬:", sorted_data)
# %%
data = [64, 34, 25, 12, 22, 11, 90]

## 내림차순 정렬 - sorted(a, reverse=True)
sorted_data = sorted(data, reverse=True)
print("내림차순 정렬:", sorted_data)
# %%
data = [64, 34, 25, 12, 22, 11, 90]

## 키를 사용한 정렬 (길이를 기준으로 정렬) 
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=len)  # len() 함수를 key에 전달, key = lambda x: len(x) - 익명함수
print("길이 기준 정렬:", sorted_words)

# %%
## sorted() - 정렬 가능한 이터러블 예시
list(range(0, 10, 2))   # 2칸씩 띄어서 출력
a = list(range(0, 10))
a

a[::2]  # 2칸씩 띄어서 출력
# %%
## sort() 와 sorted() 차이

a = [6, 2, 1, 7, 8]
a = sorted(a)  # 반환값을 a에 할당
a

b = [6, 2, 1, 7, 8]
b.sort()   # b 자체가 변하는 것
b
# %%
data = [64, 34, 25, 12, 22, 11, 90]

# 기본 정렬 (오름차순)
data.sort()
print("오름차순 정렬:", data)

# 내림차순 정렬
data.sort(reverse=True)
print("내림차순 정렬:", data)

# 키를 사용한 정렬 (길이를 기준으로 정렬)
words = ["apple", "banana", "cherry", "date"]
words.sort(key=len)
print("길이 기준 정렬:", words)
# %%
