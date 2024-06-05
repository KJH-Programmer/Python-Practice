def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("0으로 나눌 수 없습니다.")
        return None
    return a / b

def power(base, exponent):
    return base ** exponent

def sqrt(number):
    if number < 0:
        print("음수의 제곱근을 계산할 수 없습니다.")
        return None
    return number ** 0.5