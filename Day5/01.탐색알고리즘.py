# recursive.py

## 팩토리얼 ##

# 5! = 5 x 4 x 3 x 2 x 1
#    = 5 x 4!
# 4! = 4 x 3!
# 3! = 3 x 2!

def factorial(n):
    print(f"{n} * factorial({n - 1})")
    if n == 0:
        return 1
    return n * factorial(n - 1)
factorial(5)
print()

def factorial(n):
    if n == 0:    # 종료 조건
        return 1
    print(f"{n} * factorial({n - 1})")
    return n * factorial(n - 1)
print(factorial(5))  # 120
print()


## 피보나치 수열 f(n) = f(n - 1) + f(n - 2)
# 1, 1, 2, 3, 5, 8, 13, 21, 34(9번쨰) ...
def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(9))  # 너무 많아서 오류

def fibonacci(n):
    if n == 0:   # 종료조건 0, 1
        return 0
    if n == 1: # fibonaaci(1) = 1
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(9))  # 34
print()

# 팩토리얼 반복문
def factorial_iterative(n):
    result = 1
    # 1 x 2 x 3 x 4 x 5
    # n이 5일때,  1,2,3,4,5
    for i in range(1, n+1):
        result *= i
        print(f'{i}번째, result={result}')
factorial_iterative(5) # 120, 5x4x3x2x1   
print() 

# 피보나치 수열 f(n) = f(n - 1) + f(n - 2)
# 1, 1, 2, 3, 5, 8, 13, 21, 34(9번쨰) ...
def fibonacci_iterative(n):
    a, b = 0, 1
    # temp = 0

    # 0, 1, 2, 3 ..., 8
    for i in range(n):
        print(f'a={a}, b={b}')
        # temp = b
        # b = a + b
        # a = temp

        a, b = b, a+b
    return a    

print(fibonacci_iterative(9)) # 34    

# # 백준 입력 받는 법
# a, b = map(int, input().split())
# # 결과 출력 하는 법
# print(a+b)


## 백준 재귀-팩토리얼 2
# n! = n * n(n - 1)
# a = int(input())
n = int(input())
def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1) 
print(fac(n))

## 백준 재귀-피보나치 5
# f(n) = f(n - 1) + f(n - 2)
n = int(input())
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(n))

## 백준 재귀-재귀의 재귀
