##빈 딕셔너리 생성
empty_dict = {}
print(type(empty_dict))
print()

## 키-값 쌍을 포함한 딕셔너리 생성
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)
print()

## 항목 접근
print(person['name'])
# print(person['hobby']) # 가지고 잊지 않은 key 를 호출하면 에러 발생
print(person.get("age"))
print()

## 항목 추가 및 수정
person["email"] = "john@example.com"  # 항목 추가
person["age"] = 31  # 항목 수정
print(person)


## 항목 제거
del person["city"]
print(person)

#del person["hobby"]  # 에러

email = person.pop("email")
print(email)  # "john@example.com"
print(person) # {'name': 'John', 'age': 31}

## 모든 항목 제거
person.clear()
print(person) 

## 딕셔너리의 주요 메소드 ##
keys = person.keys()
#print(list(keys)[0])    # 첫번째 키
if keys:
    print(list(keys)[0])  # 첫 번째 키
else:
    print("No keys found")
print(person.values())  # 값
print()
print(person.items())   # 키 - 값

for key, value in person.items():
    print(key, value)

print(person)
print()

person.update({"age": 32, "city": "Boston"})
print(person)    

## 집합 ##
my_set = {"apple", "banana", "cherry", "cherry"}   # 출력할때마다 다르게 출력됨
print(my_set)
print(type(my_set))

a = list(set([1, 2, 3, 3, 3]))   # 중복되는 숫자가 있지만 집합으로 바꿔준다.
print(a)
# [1, 2, 3, 3, 3]: 처음 리스트에는 중복된 값 3이 여러 번 포함되어 있습니다.
# set([1, 2, 3, 3, 3]): 리스트를 집합으로 변환합니다. 집합은 중복된 값을 허용하지 않기 때문에, 집합은 {1, 2, 3}이 됩니다.
# list(set([1, 2, 3, 3, 3])): 집합을 다시 리스트로 변환합니다. 결과는 [1, 2, 3]입니다.