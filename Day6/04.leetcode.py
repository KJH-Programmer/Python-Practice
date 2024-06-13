# s(땅)과 s(물) 지도를 나타내는 m x n2D 이진 그리드가 주어 지면 섬 수를 반환합니다 .grid'1''0'
# 섬은 물로 둘러싸여 있으며 인접한 육지가 수평 또는 수직으로 연결되어 형성됩니다. 
# 그리드의 네 모서리가 모두 물로 둘러싸여 있다고 가정할 수 있습니다.
# 입력: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 출력: 1
# 예 2:
# 입력: 그리드 = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 출력: 3

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(x, y):
            if x in range(len(grid)) and \
               y in range(len(grid[0])) and \
               grid[x][y] == '1':
                    grid[x][y] = '0'
                    dfs(x + 1, y)
                    dfs(x, y + 1)
                    dfs(x - 1, y)
                    dfs(x, y - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1  # 섬의 갯수
        return count
    
grid = [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]
Solution = Solution()
result = Solution.numIslands(grid)
print(result)