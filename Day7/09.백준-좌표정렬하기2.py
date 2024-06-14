arr = []
for i in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x: (x[1], x[0]))

for x in arr:
    print(f"{x[0]} {x[1]}")