## < 프로그래머스 > ##
 
## 폰켓몬 ##
def solution(nums):      
    n = len(nums) / 2        # 가져갈 수 있는 포켓몬 수
    types = len(set(nums))   # 포켓몬의 종류
    return min(n, types)

## 완주하지 못한 선수 ##
def solution(participant, completion):
    for c in completion:
        participant.remove(c)
    print(participant)
    
    return participant[0]

## 위 코드는 효율이 떨어짐

def solution(participant, completion):
    p_dict = {}
    
    for p in participant:
        if p not in p_dict:
            p_dict[p] = 1       # p_dict 에 없는 참가자면, "이름":1 로 저장하겠다.
        else:
            p_dict[p] += 1
        
    print(p_dict)
    return

## 방법 1
from collections import defaultdict

def solution(participant, completion):
    p_dict = defaultdict(int)
    
    for p in participant:
        p_dict[p] += 1
    
    for c in completion:
        p_dict[c] -= 1
        if p_dict[c] == 0:
            del p_dict[c]
            
    return list(p_dict.keys())[0]

## 방법2
from collections import Counter

def solution(participant, completion):
    p_dict = Counter(participant)
    c_dict = Counter(completion)
    
    answer = p_dict - c_dict
    return list(answer.keys())[0]