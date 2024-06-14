class solution:
    def combine(self, n, k):
        results = []
        stack = [(1, [])]

        while stack:
            start, elements = stack.pop()   
            if len(elements) == k:
                results.append(elements[:])
                continue

            for i in range(start, n + 1):
                stack.append((i+1, elements+[i]))

        return results
sol = solution()
results = sol.combine(4, 2)
print(results)    

# result는 최종결과를 저장할 리스트이고, stack은 초기 스택 상태인데 '1'은 조합에 추가할 수의 시작값이고 \
# '[ ]'은 현재까지의 조합입니다. 그리고 stack이 비어있지 않은 동안 반복문을 돌려주고 \
# 스택이 비어있으면 모든 가능한 조합을 탐색한 것이 됩니다. \
# stack 에서 요소들을 꺼내와서 'start'와 'elements' 에 할당합니다. \
# 여기서 'start'는 다음에 추가할 수의 시작값, 'element'는 현재까지의 조합 인데 \
# elements 의 길이가 k와 같다면 element 값을 results 에 추가하고 다음 반복으로 넘어갑니다. \
# 요소 순환 부분에서는 'start'부터 n+1 까지 숫자들을 반복하며 i 에 넣어주면서 \
# (i + 1, elements + [i]) 을 stack 에 추가를 해주는데 여기서 i + 1 은 다음에 추가할 수의 값 이고 \
# elements + [i] 는 새로운 조합이다. 그러고 results 값을 반환해준다.