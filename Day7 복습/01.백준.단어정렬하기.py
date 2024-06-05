n = int(input())  # 13
vars = set()  # 중복을 없애기위해

for _ in range(n):
    var = input()
    vars.add(var)
sorted_vars = sorted(vars, key=lambda x: (len(x), x))    # 튜플로 묶어서 여러가자로 정렬 -> (길이를기준으로 정렬, 사전 그대로 정렬)

for var in sorted_vars:
    print(var)

## 방법 2 ##
# 자료를 추가 -> 정렬 -> 출력
n = int(input())
words = set(input() for _ in range(n))  # 제너레이터 표현식

sorted_words = sorted(words, key=lambda x: (len(x), x))    # 튜플로 묶어서 여러가자로 정렬 -> (길이를기준으로 정렬, 사전 그대로 정렬)

for var in sorted_words:
    print(var)

## 방법 3
# 정렬이 된 상태로 자료를 추가 -> 출력
import heapq
n = int(input())
heap = list()
words = set()
for _ in range(n):
    word = input()
    # heap 배열에 item 을 추가해주겠다. (정렬된 상태로)
    heapq.heappush(heap, word)

while heap:
    word = heapq.heappop(heap)
    print(word)