## 대표값2 ##
import sys
input = sys.stdin.readline

# arr = []
# for _ in range(n):
#     arr.append(int(input()))
arr = [int(input()) for _ in range(5)]    

평균 = int(sum(arr) / len(arr))
중앙값 = sorted(arr)[2]

print(평균)
print(중앙값)