## 복습문제 ##
# 문제1 : 함수

def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print(greet("Alice")) # 출력: "Hello, Alice!"
print(greet("Bob", greeting="Hi")) # 출력: "Hi, Bob!"
print(greet("Charlie", "Hey", punctuation="!!")) # 출력: "Hey, Charlie!!"
print()

# 문제2 : 예외 처리

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(divide(10, 2))
print(divide(10, 0))
print()

# 문제3 : 모듈
from mymath import add, multiply
print(add(3, 5))
print(multiply(3, 5))
print()

# 문제4 : 클래스
class Animal:
    def __init__(self, name):   # 생성자에서 동물이름만 가져오기때문에 name 만 매개변수로 넣어준다.
        self.name = name

    def speak(self):
        return "어떤 소리를 냅니다"  # 밑에 print()문으로 반환하기때문에 return후에 "~~" 바로 입력해준다.

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

animals = [Dog("렉스"), Cat("위스커스"), Animal("제네릭")]  # 생성자
for animal in animals:
    print(f"{animal.name}(이)가 {animal.speak()}")