# 다음 코드에서 list_methods 함수를 완성하세요.
def list_methods(my_list):
    # 1. 3을 리스트의 맨 끝에 추가하세요
    my_list.append(3)
    # 2. 5를 리스트의 첫 번째 위치에 추가하세요
    my_list.insert(0, 5)
    # 3. 리스트의 첫 번째 요소를 제거하세요
    my_list.pop(0)
    # 4. 리스트를 오름차순으로 정렬하세요
    my_list.sort()

example_list = [4, 2, 1, 5]
list_methods(example_list)
print(example_list)  # 출력: [1, 2, 3, 4, 5]