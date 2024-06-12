# 다음 코드에서 check_duplicate_keys 함수를 완성하세요.
def check_duplicate_keys(dict1, dict2):
    # 여기에 코드를 작성하세요
    for key in dict2:
        if key in dict1:
            print(f'key {key} is duplicated')
    
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
check_duplicate_keys(dict1, dict2)
# 출력:
# Key b is duplicated