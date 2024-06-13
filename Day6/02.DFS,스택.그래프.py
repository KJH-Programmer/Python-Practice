graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        print(f'while문 진입 - 앞으로 탐색할 노드들 {stack=}')
        v = stack.pop()
        print(f'stack에서 값을 하나 뺌: {v=}')
        if v not in discovered:
            print(f'아직 탐색에 추가되지 않은 v 추가 {discovered=}')
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
                print(f'정점 {v=}와 연결된 장점 연결된 정점 {w=}를 다음 탐색 스택에 추가')
    return discovered

print(f'{iterative_dfs(1)=}')