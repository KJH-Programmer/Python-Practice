n = int(input())
# Coordinates
coords = [list(map(int, input().split())) for _ in range(n)]
coords.sort()
for x, y in coords:
    print(x, y)

# 예제 입력 1
# 5
# 0 4
# 1 2
# 1 -1
# 2 2
# 3 3

# 예제 출력 1
# 1 -1
# 1 2
# 2 2
# 3 3
# 0 4