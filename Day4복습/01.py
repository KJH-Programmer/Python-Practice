numbers = [23, 3, 612, 354, 4]

# 정렬
numbers.sort(reverse=True)  # 내림차순
print(numbers)

# numbers = numbers.sort() # None
# print(numbers)  

## 딕셔너리 ##
# 빈 딕셔너리 생성
emptt_dict = {}

# 키-값 쌍을 포함한 딕셔너리 생성
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# items() : 딕셔너리의 모든 키-값 쌍을 반환합니다.
for key, value in person.items():
    print(key, value)

## 문자열 ##


## 시퀀스 ##
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
# zipped = zip(list1, list2)
# print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

for a, b in zip(list1, list2):
    print(a, b)
