# 다음 코드의 시간 복잡도를 분석하고 이유를 설명하세요.

def find_target_in_lists(lists, target):
    for lst in lists:
        if target in lst:
            print(f"Found {target} in list {lst}")
            return
    print(f"{target} not found in any list")

# 예시
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
find_target_in_lists(lists, 5)


# **질문:**
# 1. `find_target_in_lists` 함수의 시간 복잡도는 무엇이며, 그 이유는 무엇인가요?
# 2. `if target in lst:` 구문의 시간 복잡도와 이를 호출하는 for문이 결합되면 전체 시간 복잡도는 어떻게 계산되나요?

print("1: find_target_in_lists 함수의 시간 복잡도는 O(N^2)입니다. 이유는 외부 for문이 길이 N의 리스트들을 순회하고, \
      각 리스트에 대해 target in lst 구문을 실행하기 때문입니다.")
print("target in lst 구문의 시간 복잡도는 O(N)이고, 이를 호출하는 for문도 길이 N의 리스트를 순회하기 때문에 \
      전체 시간 복잡도는 O(N) * O(N) = O(N^2)입니다.")