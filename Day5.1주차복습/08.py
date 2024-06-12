# 다음 코드의 시간 복잡도를 분석하고 이유를 설명하세요.
def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

# 예시
arr = [1, 2, 3]

# 질문
# 1. 이 코드의 시간 복잡도는 무엇이며, 그 이유는 무엇인가요?     
# 2. 이 코드가 입력 배열 `arr`의 길이가 두 배로 증가할 때, 실행 시간은 어떻게 변하나요?