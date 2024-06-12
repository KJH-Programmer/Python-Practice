# 다음과 같은 출력을 내기 위해 describe_person 함수를 완성하세요. 
# 이 함수는 사람의 이름과 나이를 출력하며, 나이가 제공되지 않을 경우 기본값으로 0을 사용합니다.

def describe_person(name, age=0):
    return f'{name} is {age} years old'

print(describe_person("Alice", 30))  # 출력: Alice is 30 years old.
print(describe_person("Bob"))        # 출력: Bob is 0 years old.

