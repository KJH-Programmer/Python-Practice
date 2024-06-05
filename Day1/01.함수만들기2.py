print("< 함수 정의와 호출 >")
print("문제1")
#다음과 같은 함수를 정의하라. 이 함수는 두 개의 숫자를 입력받아 그 합을 반환한다. 
#그리고 이 함수를 호출하여 결과를 출력하라.
def num(x, y):
    c = x + y
    return c
num = num(3, 4)
print(num)

print("문제2")
def strings_value(value):
    return value * 3
strings_value = strings_value("hello")
print(strings_value)
###################################################
print("< 매개변수와 리턴값 >")
print("문제3")    
def num_value(value, n):
    return value * n
num_value = num_value(3, 4)
print(num_value)

print("문제4")
def string_value(values):
    return max(values, key=len)
string_value = string_value(["ccccc", "aaaaaaa", "xxx"])
print(string_value)
###################################################
print("< 가변 매개변수 >")
print("문제5")
def sum_all(*agrs):
    return sum(agrs)
num = sum_all(10, 20, 30)
print(num)

print("문제6")
def strings_blank(*values):
    return "  ".join(values)
strings_blank = strings_blank("apple", "사과")
print(strings_blank)
###################################################
print("< 기본 매개변수 > ")
print("(문제7)")
def two_num_multiply(x, y=1):
   return x * y
num1 = two_num_multiply(3)
num2 = two_num_multiply(3, 4)
print(num1)
print(num2)

print("(문제8)")
def string_repeat_num(x, y=1):
    return x * y
print(string_repeat_num("안녕"))
print(string_repeat_num("안녕", 3))    

###################################################
print("< 키워드 매개변수 >")

print("(문제9)")
def string_values(name, age):
    print(f"name : {name}, age : {age}")
string_values(name="지훈", age=28)

print("(문제10)")
def kwargs_num(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
kwargs_num(name="Alice", age=30, city="New York")

