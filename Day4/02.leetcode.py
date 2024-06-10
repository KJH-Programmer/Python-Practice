## 유효한 펠린드롬
# 모든 대문자를 소문자로 변환하고 영숫자가 아닌 모든 문자를 제거한 후 앞뒤로 동일하게 읽는 경우 구문 은 회문 입니다. 
# 영숫자 문자에는 문자와 숫자가 포함됩니다.
# 주어진 문자열이 회문 이면 반환하고, 그렇지 않으면s 반환합니다. truefalse


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 알파벳만 남기기
        s = [letter.lower() for letter in s if letter.isalnum()]
        return s == s[::-1]

        # new_s = ""
        # for letter in s:
        #     if letter.isalnum():
        #         new_s += letter
        # new_s = new_s.lower()

        # return new_s == new_s[::-1]
    #     new_array = list(new_s)
                
    #    while len(new_array) > 2:     # 종료 시점을 모를때 while 문 사용
    #         # 마지막 값과 첫번째 값 추출
    #         if new_array.pop() != new_array.pop(0):
    #             return False 

    #     return True 