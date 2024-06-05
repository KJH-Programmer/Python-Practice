# 문자열을 정수로 변환

number = int("100")
print(number)
print(type(number))


string = "-100"
try:
    number = int(string)
    print(number)
    print(type(number))
except:
    print("숫자로 변환할 수 없음")    
