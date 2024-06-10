## 문자열의 기본연산 ##

## 인덱싱
word = "python"
print(word[0])
print(word[-1])

## 슬라이싱
# [start:end:stride]
word = "python"
print(word[0:len(word):1])  # 0부터 word의 길이까지 가격을 1로 해서 출력
print(word[::-1])  # 역순
print(word[:])  # 전체 출력

## 길이 확인
print(len(word))

## 문자열 결합 * 결합
greeting = "hello, " + "world!"
print(greeting)

echo = "Hello! " * 3
print(echo)

## 문자열 주요 메소드 ##

## 문자열 분할
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)            # ['apple', 'banana', 'cherry']

text = "apple,  banana,  cherry"
fruits = text.split(",")
print(fruits)            # ['apple', '  banana', '  cherry']

# # 반복문
# for i, fruits in enumerate(fruits):
#     fruits[i] = fruits.strip()

# # 고차함수
# fruits = list(map(lambda x: x.strip(), fruits))

# 리스트 컴프리헨션
fruits = [fruit.strip() for fruit in fruits]  
print(fruits)

## 문자열 결합
text = ",".join(fruits)   # ,기준으로 나눠준다.
print(text)

## 문자열 검색 및 대체
text = "hello, world"
print(text.find("world"))  # 인덱스 7 번 부터 world 가 등장
print(text.replace("world", "python"))

## 문자열 포메팅 ##
# f-string (추천)
name = "John"
age = 30
text = f"My name is {name} and I am {age} years old."
print(text)    # 'My name is John and I am 30 years old.'