class Solution:
    def updateMatrix(self, matrix: list) -> list:
        m = len(matrix)
        n = len(matrix[0])
        dist = list(list(-1 for i in range(n)) for j in range(m))
        level = set((i,j) for j in range(n) for i in range(m) if matrix[i][j] == 0)
        visited = set()
        d = 0
        while level:
            for x,y in level:
                dist[x][y] = d
            d += 1
            visited |= level
            level = set((x+i,y+j) for x,y in level for i,j in [[0,1],[0,-1],[1,0],[-1,0]] if 0 <= x+i < m and 0 <= y+j < n and not (x+i,y+j) in visited)
        return dist

ans = Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
print(ans)