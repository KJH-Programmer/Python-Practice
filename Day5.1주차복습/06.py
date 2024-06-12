# 다음은 `random` 모듈의 `randint` 함수에 대한 설명입니다. 
# 설명을 읽고 적절하게 `randint` 함수를 사용하여 문제를 해결하세요.
# **함수 설명:**
# `random.randint(a, b)`는 a와 b 사이의 랜덤 정수를 반환합니다 (a와 b를 포함).
# 다음과 같은 출력을 내기 위해 `generate_lotto_numbers` 함수를 완성하세요. 
# 로또 번호는 1부터 45 사이의 중복되지 않는 6개의 숫자여야 합니다.

import random

def generate_lotto_numbers():
    # 여기에 코드를 작성하세요
    nums = set()
    while len(nums) < 6:
        num = random.randint(1, 45)
        nums.add(num)
    return list(nums)    
    #return random.sample(range(1, 46), 6)

print(generate_lotto_numbers())  # 출력: 1부터 45 사이의 중복되지 않는 6개의 숫자가 리스트로 출력됩니다 (예: [3, 12, 25, 33, 37, 41])
