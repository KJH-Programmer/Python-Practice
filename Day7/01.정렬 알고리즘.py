## 버블 정렬 ##
def bubble_sort(arr):
    # 배열의 길이
    n = len(arr)

    # 이중 반복문
    for i in range(n):
        for j in range(0, n - i - 1):  # i 가 0 일때는 (0, 7 - 0 - 1) => range(6)/ i = 1 (0, 6 - 0 -1) => range(5)
            if arr[j] > arr[j + 1]:   # 현재요소가 다음요소보다 클때
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 두 요소 위치를 바꾼다.
                # 예를 들어 j=0 이면 64, j+1 은 34 인데 현재요소인 64가 더 크기때문에 위치를 바꿔서 34, 64 가 된다.
                print(arr)                
    return arr

# 테스트
data = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort 결과:", bubble_sort(data))    # Bubble Sort 결과: [11, 12, 22, 25, 34, 64, 90]
print()

## 삽입 정렬 ##
def insertion_sort(arr):
    # range(1, 7) -> 1, 2, 3, 4, 5, 6
    for i in range(1, len(arr)):
        # 정렬할 값 지정
        key = arr[i]  # arr[1] ... arr[6]
        # 정렬할 값의 왼쪽 인덱스 가져오기
        j = i - 1  # 0, 1, 2, 3, 4, 5

        # 앞에 있는 값이 뒤에 있는 값보다 클 때 까지
        # 정렬이 안되어있다면, j가 음수이면 list out of 에러가 뜨기때문에
        while j >= 0 and key < arr[j]:
            #print(f'정렬 전: {arr=}, {j+1=}, {j=}')
            arr[j + 1] = arr[j]

            #print(f'정렬 후: {arr=}, {j+1=}, {j=}')
            j -= 1
        #print(f'{key=}, {j+1=}')    

        # j 인덱스를 가장 왼쪽까지 이동시킨 후 값 복구
        arr[j + 1] = key

    return arr

# 테스트
data = [64, 34, 25, 12, 22, 11, 90]
print("Insertion Sort 결과:", insertion_sort(data))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
