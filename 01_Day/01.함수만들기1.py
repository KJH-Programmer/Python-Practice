# 문제 1
print("< 실습문제 1 >")
def add(x, y):
    c = x + y
    return c
c = add(7, 3)
print(c)

print("< 실습문제 2 >")
def repeat_string(value, n):
    return value * n
repeat_string = repeat_string("hello", 3)
print(repeat_string)

print("< 실습문제 3 >")
def sum_all(*values):
    return sum(values)
number = sum_all(10, 20, 30)
print(number) # 60
number = sum_all(10, 20, 30, 40, 50)
print(number) # 150

print("< 실습문제 4 >")
def multiply(values, n=1):
    return values * n
result = multiply(7, 3)
print(result)
result = multiply(7)
print(result)

print("< 실습문제 5 >")
def print_info(name, age):
    print(f"name : {name}, Age : {age}")
print_info(name="Alice", age=30)
print_info(age=25, name="Bob")

print("< 심화문제 1 >")
def add_and_multiply(a, b):
    return a + b, a * b
sum_result, product_result = add_and_multiply(5, 3)
print(f"Sum: {sum_result}, Product: {product_result}")

print("< 심화문제 2 >")
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="Alice", age=30, city="New York")

print("< 심화문제 3 >")
#혼합 매개변수를 사용하는 함수를 정의하라. 이 함수는 필수 
#매개변수 두 개와, 기본 매개변수 하나, 가변 매개변수 하나, 키워드 가변 매개변수 하나를 받아
#각각을 출력한다. 그리고 이 함수를 호출하여 결과를 출력하라.
def mixed_params(a, b, c=0, *args, **kwargs):     # https://www.tensorflow.org/api_docs/python/tf/keras/Model 참고
    # a, b = 위치 인수, 항상 값을 전달 받아야함
    # c = 기본값이 있는 위치 인수, 값이 제공되지 않으면 기본값 0 을 사용SS
    # *args = 가변 위치 인수, 전달된 위치 인수의 나머지를 튜플 형태로 받음
    # **kwargs = 가변 키워드 인수, 전달된 키워드 인수의 나머지를 딕셔너리 형태로 받음
    print(f"a: {a}, b: {b}, c: {c}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
mixed_params(1, 2)
mixed_params(1, 2, 3, 4, 5, 6, key1="value1", key2="value2")