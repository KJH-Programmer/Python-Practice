#print("hello world")

#print(len('Hello')) # 5

# p.275
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
print_3_times()

# p.276
def print_n_times(value, n):
    for i in range(n):
        print(value, i)
print_n_times("안녕하세요", 5)

# p.278
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
            print(type(values))   # value 의 형태 확인 -> <class 'tuple'>
        print()
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")  

# p.279
def print_n_times(value, n=2):
    for i in range(n):
        print(value)
print_n_times("안녕하세요")

# p.283 키워드 매개변수
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()    
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)

# p.290 ~ 291
print("< 확인문제 1 >")
def f1(x):
    return x
print(f1(5))

def f2(x):
    return (x * 2) + 1
print(f2(5))

def f3(x):
    return (x**2) + (x * 2) + 1
print(f3(5))


print("< 확인문제 2 >")
def mul(*values):
    result = 1
    for value in values:
        result = result * value
        #result *= value
    return result
print(mul(5, 7, 9, 10))


print("< 확인문제 3 >")
# def function(*values, valueA, valueB):
#     pass
# function(1,2,3,4,5)
