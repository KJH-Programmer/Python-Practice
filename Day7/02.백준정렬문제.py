n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:   
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  

    return arr
bubble = bubble(arr)
print(bubble)    # [1, 2, 3, 4, 5]


# n = int(input())

# arr = []
# for _ in range(n):
#     arr.append(int(input()))

# def bubble(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             # 이전값이 뒤에 있는 값보다 크면
#             if arr[j] > arr[j + 1]:
#                 arr[j + 1], arr[j] = arr[j], arr[j + 1]
# print(arr)
# bubble(arr)
# print(arr)                