from functools import cmp_to_key

# 오름차순
# 값이 4라면 맨앞으로 정렬
def compare(x, y):
    if x > y:
        return 1
    else:
        return -1
a = ["abcd", "zxc", "q"]

print(sorted(a, key=cmp_to_key(compare)))