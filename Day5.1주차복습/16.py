def add_element(my_set, element):
    # 여기에 코드를 작성하세요
    my_set.add(element)
    
original_set = {1, 2, 3}
add_element(original_set, 4)
print(original_set)  # 출력: {1, 2, 3, 4}

add_element(original_set, 5)
print(original_set)  # 출력: {1, 2, 3, 4, 5}