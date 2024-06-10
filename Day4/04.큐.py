from collections import deque

queue = deque()

# enqueue 연산
queue.append(1)
queue.append(2)
queue.append(3)

# dequeue 연산
front_element = queue.popleft()  # front_element는 1이 됨

# peek 연산
front_element = queue[0]  # front_element는 2가 됨

# is_empty 연산
is_empty = len(queue) == 0
print(queue, front_element)

deq = deque([1, 2, 3, 4, 5])

# rotate
deq.rotate(1)
print(deq)
