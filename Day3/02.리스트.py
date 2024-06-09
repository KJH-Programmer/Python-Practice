## 리스트 기본 연산 ##
numbers = [10, 20, 30, 40, 50]

# 원소의 첫 번째 접근, 0번째 인덱스 접근
print(numbers[0])  # 10

# 원소의 마지막에 접근
print(numbers[-1]) # 50 (역순 인덱스)

# 원소의 항목 변경
numbers[0] = 100
print(numbers)  # [100, 20, 30, 40, 50]

# 항목 추가
numbers.append(60)
print(numbers)  # [100, 20, 30, 40, 50, 60]

# 항목 삽입
numbers.insert(2, 25)
print(numbers)  # [100, 20, 25, 30, 40, 50, 60]

# 항목 제거
numbers.remove(30)
print(numbers)  # [100, 20, 25, 40, 50, 60]

try:
    numbers.remove(30)
except:
    pass
print(numbers)

# 항목 팝(pop), 맨 뒤에 값을 지워줌
last_item = numbers.pop()
print(last_item)  # 60
print(numbers)    # [100, 20, 25, 40, 50]

# 항목 포함 여부 확인, in
print(20 in numbers)  # True
print(70 in numbers)  # False

######## 리스트의 주요 메소드 ##########
# extend() : 리스트에 다른 리스트나 반복 가능한 객체의 모든 항목을 추가합니다.
numbers.extend([70, 80])
print(numbers)  # [100, 20, 25, 40, 50, 70, 80]

# sort() : 리스트를 정렬
numbers.sort()
print(numbers)  # [20, 25, 40, 50, 70, 80, 100]

numbers.sort(reverse=True)  # 내림차순으로 보여줌, [100, 80, 70, 50, 40, 25, 20]
print(numbers)

# reverse() : 리스트의 항목 순서를 반대로 뒤집습니다
numbers.reverse()
print(numbers)  # [20, 25, 40, 50, 70, 80, 100]

numbers = numbers[::-1]  # reverse() 와 동일한 역할
print(numbers)  # [100, 80, 70, 50, 40, 25, 20]

# index(): 특정 항목의 첫 번째 인덱스를 반환합니다.
index = numbers.index(50)
print(index)  # 3

# count(): 리스트 내에서 특정 항목이 몇 번 등장하는지 반환합니다.
count = numbers.count(25)
print(count)  # 1