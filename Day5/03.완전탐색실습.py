## 실습1 : 배열의 모든 부분 집합 찾기
def find_subsets(arr):
    subsets = [[]]
    for num in arr:
        subsets += [current + [num] for current in subsets]
    return subsets

# 테스트
arr = [1, 2, 3]
subsets = find_subsets(arr)
for subset in subsets:
    print(subset)
print()

## 실습2 : 문자열의 모든 순열 찾기
def permute(s):
    result = []
    stack = [('', s)]

    while stack:
        perm, chars = stack.pop()
        if not chars:
            result.append(perm)
        else:
            for i in range(len(chars)):
                stack.append((perm + chars[i], chars[:i] + chars[i+1:]))
    return result

# 테스트
s = "ABC"
permutations = permute(s)
for perm in permutations:
    print(perm)
print()

## 실습3 : 두 수의 모든 조합 찾기
def find_combinations(list1, list2):
    combinations = []
    for num1 in list1:
        for num2 in list2:
            combinations.append((num1, num2))
    return combinations

# 테스트
list1 = [1, 2]
list2 = [3, 4]
combinations = find_combinations(list1, list2)
for combo in combinations:
    print(combo)

## 실습4 : 1부터 N까지의 숫자의 모든 순열 찾기


