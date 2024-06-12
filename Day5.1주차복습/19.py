def set_methods(my_set):
    # 1. 5를 집합에 추가하세요
    my_set.add(5)
    # 2. 3을 집합에서 제거하세요
    my_set.remove(3)
    # my_set.discard(3)
    # 3. 집합이 비어있는지 확인하세요
    is_empty = len(my_set) == 0
    return is_empty

example_set = {1, 2, 3, 4}
is_empty = set_methods(example_set)
print(example_set)  # 출력: {1, 2, 4, 5}
print(is_empty)     # 출력: False