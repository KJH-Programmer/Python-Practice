# 다음과 같은 출력을 내기 위해 divide 함수를 완성하세요. 이 함수는 두 숫자를 나누며, 
# 두 번째 숫자가 0일 경우 예외를 처리하여 "Cannot divide by zero"를 출력합니다.
def divide(a, b):
    try:
        # 여기에 코드를 작성하세요
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
        # 여기에 코드를 작성하세요

result = divide(10, 2)
print(result)  # 출력: 5.0

result = divide(10, 0)
print(result)  # 출력: Cannot divide by zero