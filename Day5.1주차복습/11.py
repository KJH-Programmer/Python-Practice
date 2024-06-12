# 다음 코드에서 list_operations 함수를 완성하세요
def list_operations(my_list):
    # 여기에 코드를 작성하세요
    sum_of_elements = sum(my_list)
    max_element = max(my_list)
    min_element = min(my_list)
    length_of_list = len(my_list)
    return sum_of_elements, max_element, min_element, length_of_list

example_list = [1, 2, 3, 4, 5]
result = list_operations(example_list)
print(result)  # 출력: (15, 5, 1, 5)