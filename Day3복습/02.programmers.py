# n 번째 원소까지
def solution(num_list, n):
    answer = num_list[0:n]
    return answer

# def solution(num_list, n):
#     return num_list[0:n]

# n번째 원소부터
def solution(num_list, n):
    answer = num_list[n-1:]
    return answer

# 첫번째 나오는 음수
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1

# solution 함수에 num_list를 배개면수로 받고
# num_list - 1 까지의 수를 i 에 넣어 반복한다.
# 만약 인덱스i번째 num_list 가 0 보다 작을때 i 를 반환해준다.
# for문을 돌렸을때 만족하지않으면 -1 을 반환해준다.

def solution(num_list):
    for i, num in enumerate(num_list):
        if num < 0:
            return i
    return -1

# 카운트 다운
