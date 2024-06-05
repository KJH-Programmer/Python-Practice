# 2번
a, b = map(int, input().split())
print(a + b)

## 반복문 ##
# 1번
def solution():
    A, B = map(int, input().split())   
    # input()으로 입력값을 받음
    # split() 함수로 공백을 기준으로 문자열을 나눠서 리스트로 반환 ["1", "2"]
    # map(int, 문자열) 함수를 사용하여 위에서 공백으로 나누어진 문자열을 정수로 변환 [1, 2]
    
    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("==")
        
solution()
# 1 2 를 입력하면 < 이 출력된다.
