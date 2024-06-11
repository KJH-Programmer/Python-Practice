import heapq

# 빈 힙 생성
min_heap = []

# 삽입 연산
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 2)
print(min_heap)

min_value = heapq.heappop(min_heap)
min_value = heapq.heappop(min_heap)
min_value = heapq.heappop(min_heap)

print(min_value)
print(min_heap)

# 빈 우선 순위 큐 생성
priority_queue = []

# 우선 순위와 함께 삽입 (우선 순위, 값)
heapq.heappush(priority_queue, (1, '밥먹기'))
heapq.heappush(priority_queue, (3, '운동하기'))
heapq.heappush(priority_queue, (2, '자기'))

# 우선 순위가 가장 높은 요소 제거 및 반환
priority_task = heapq.heappop(priority_queue)
print(priority_task)  # 출력: (1, '밥먹기')


