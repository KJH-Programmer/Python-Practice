# main.py
import calculator

def main():
    # 더하기 예시
    result = calculator.add(10, 5)
    print(f"10 + 5 = {result}")

    # 빼기 예시
    result = calculator.subtract(10, 5)
    print(f"10 - 5 = {result}")

    # 곱하기 예시
    result = calculator.multiply(10, 5)
    print(f"10 * 5 = {result}")

    # 나누기 예시
    result = calculator.divide(10, 5)
    print(f"10 / 5 = {result}")

    # 0으로 나누기 예시
    result = calculator.divide(10, 0)
    if result is not None:
        print(f"10 / 0 = {result}")

    # 거듭제곱 예시
    result = calculator.power(2, 3)
    print(f"2^3 = {result}")

    # 제곱근 예시
    result = calculator.sqrt(9)
    print(f"sqrt(9) = {result}")

    # 음수의 제곱근 예시
    result = calculator.sqrt(-9)
    if result is not None:
        print(f"sqrt(-9) = {result}")

if __name__ == "__main__":
    main()
# if문 안에있는 함수를 실행할건데 main() 함수부터 실행한다.

##########################################
import calculator

a, b = map(int, input().split())
print(f"a는 {a}")
print(f"b는 {b}")
print(f"a는 {type(a)}")
print(f"b는 {type(b)}")

print(calculator.add(a, b))
print(calculator.subtract(a, b))
print(calculator.multiply(a, b))
print(calculator.divide(a, b))
print(calculator.divide(10, 0))
print(calculator.sqrt(100))
print(calculator.sqrt(-100))

# 방향키 기준으로 컨트롤+알트 방향키 키워드선택
# 컨트롤 + D 키워드 전체선택