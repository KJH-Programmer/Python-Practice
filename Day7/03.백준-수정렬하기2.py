## 수 정렬하기 2 ## 
## 방법 1
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)   # 정렬된 새로운 리스트를 할당

for element in arr:
    print(element)
# 입력예시          출력예시
# 5                 1
# 5                 2
# 4                 3
# 3                 4
# 2                 5
# 1 
# -> 첫번째 5는 n 이라고 생각/ 5줄을 받아오는 개념

# n 이라는 사용자 입력값을 정수형으로 받는 변수를 만들어준다
# arr 이라는 빈리스트로 초기화를 시켜주고
# 입력받은 n 을 순회하면서 arr 에 정수형으로 변환후에 추가해준다.
# arr 를 정렬 후에 다시 저장해주고 element에 순회하면서 넣어주고 출력해준다.






## 방법2
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()         #  arr 자체 정렬

for element in arr:
    print(element)


