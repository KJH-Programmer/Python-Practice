# 다음 코드에서 add_entry 함수를 완성하세요.
def add_entry(my_dict, key, value):
    # 여기에 코드를 작성하세요
    my_dict[key] = value

original_dict = {'a': 1, 'b': 2}
add_entry(original_dict, 'c', 3)
print(original_dict)  # 출력: {'a': 1, 'b': 2, 'c': 3}

add_entry(original_dict, 'd', 4)
print(original_dict)  # 출력: {'a': 1, 'b': 2, 'c': 3, 'd': 4}