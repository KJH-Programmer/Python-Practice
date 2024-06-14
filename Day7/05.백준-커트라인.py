n, m = map(int, input().split())
# n, m = int(n), int(m)
scores = list(map(int, input().split()))
scores.sort(reverse=True)
print(scores[m - 1])

# 예제 입력 1
# 5 2
# 100 76 85 93 98

# 출력 1
# 98

