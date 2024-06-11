## 순열
# 순열을 구하는 함수

# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (3, 1, 2)
# (3, 2, 1)

# 재귀 #
def permute(data, depth, n, result):
    if depth == n:
        print(result)
        return

    for i in range(len(data)):
        if data[i] not in result:
            result.append(data[i])
            permute(data, depth + 1, n, result)
            result.pop()

data = [1, 2, 3]
permute(data, 0, len(data), [])
print()

# 스택 #
def permute(data):
    result = []
    stack = [([], data)]

    while stack:
        print(stack)
        perm, items = stack.pop()
        #if not items:
        if len(items) == 0:
            result.append(perm)
        else:
            for i in range(len(items)):
                new_perm = perm + [items[i]]  
                new_items = items[:i] + items[i+1:]
                stack.append((new_perm, new_items))

    return result

data = [1, 2, 3]
permutations = permute(data)
for perm in permutations:
    print(perm)
print()


# 노션 실습 #
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

## 백준 블랙잭 ##
# 방법 1
# 입력
a, b = map(int, input().split())
cards = list(map(int, input().split()))

reuslt = 0
for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            if cards[i] + cards[j] + cards[k] > b:
                continue
            else:
                reuslt = max(reuslt, cards[i] + cards[j] + cards[k])
print(reuslt)                

# 방법 2
a, b = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            number = cards[i] + cards[j]+ cards[k]
            if number <= b and \
               number > result:
                result = number
print(result)

## 백준 분해합 ##
n = int(input())
printed = False
# 1부터 시작해서 n 까지 훓어본다
# 가장먼저 합이 n 이되는 수를 리턴
for number in range(1, n+1):
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)
    #sum_of_digits = sum([int(digit) for digit in str(number)])
    if number + sum_of_digits == n:
        printed = True
        print(number)
        break
if printed == False:
    print(0)

## 백준 수학은 비대면강의 ##
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)         

