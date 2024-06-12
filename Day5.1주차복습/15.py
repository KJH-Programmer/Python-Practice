def dict_methods(my_dict):
    # 1. 'd': 4 항목을 추가하세요
    my_dict['d'] = 4
    # 2. 'a' 항목을 제거하세요
    del my_dict['a']
    # 3. 딕셔너리를 키 기준으로 정렬된 리스트로 반환하세요
    return sorted(my_dict.items())    

example_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = dict_methods(example_dict)
print(sorted_dict)  # 출력: [('b', 2), ('c', 3), ('d', 4)]