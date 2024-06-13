## f-string 더 간편한 방법 ##
# number = 100
# print(f"number={number}")
# print(f'{number=}')
# # 출력결과 : number=100

# 1 ~ 7 번에 해당하는 key가 정점
graph = {
    1: [2, 3, 4], # 부모 노드
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def recursive_dfs(v, discovered=[]):  # v : vertex(정점) 
    print(f'탐색하는 정점- {v}, 여태까지 경로:{discovered}')
    # 우리가 탐색한 경로
    discovered.append(v)
    print(f'recrusive_dfs 진입- 여태까지 경로 {discovered}')
    print(f'append 함수 호출- 탐색한 정점 {v}와 연결된 노드들은 {graph[v]}이고 연결된 노드들을 하니씩 탐색합니다.')
    for w in graph[v]:   # graph[v] : 정점과 연결된 다른 정점
        if w not in discovered:  # 이미 탐색한 정점은 거르기
            print(f'if문 진입- 정점 {w}는 아직 탐색하지 않았기 때문에 재귀함수를 호출합니다.')
            discovered = recursive_dfs(w, discovered)
            print(f'제귀함수 종료- 정점 {w}에 대한 재귀함수가 종료되었습니다.')
    return discovered
    
print(f'{recursive_dfs(1)=}')