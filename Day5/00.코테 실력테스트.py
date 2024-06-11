def solution(s):
    number_dict = {"zero":0, "one":1, "two":2, "three":3, "four":4, 
              "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    new_s = ""
    temp = ""
    
    for letter in s:
        #print(temp)
        if letter.isdigit():  # 숫자 확인 메소드
            new_s += letter
        else:
            temp += letter
            if temp in number_dict:
                new_s += str(number_dict[temp])
                temp = ""
    return int(new_s)

print(solution("one4seveneight"))
print(solution("23four5six7"))