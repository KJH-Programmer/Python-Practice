def dict_operations(my_dict):
    # 여기에 코드를 작성하세요
    keys = list(my_dict.keys())     # 리스트 처럼 사용하기위해 list 로 감싸준다.
    values = list(my_dict.values())
    length_of_dict = len(my_dict) 
    return keys, values, length_of_dict

example_dict = {'a': 1, 'b': 2, 'c': 3}
result = dict_operations(example_dict)
print(result)  # 출력: (['a', 'b', 'c'], [1, 2, 3], 3)