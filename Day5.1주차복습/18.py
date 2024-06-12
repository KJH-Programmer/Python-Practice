def set_operations(set1, set2):
    # 여기에 코드를 작성하세요
    union_set = set1.union(set2)     # 합집합
    #union_set = set1 | set2
    intersection_set = set1.intersection(set2)    # 교집합
    #intersection_set = set1 & set2
    difference_set = set1.difference(set2)    # 차집합
    #difference_set = set1 - set2
    return union_set, intersection_set, difference_set

set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set_operations(set1, set2)
print(result)  # 출력: ({1, 2, 3, 4}, {2, 3}, {1})