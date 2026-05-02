class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        rows,cols = len(grid), len(grid[0])
        dist = 0
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        while q:
            r,c = q.popleft()
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc

                if 0<= nr<rows and 0<=nc<cols and grid[nr][nc] == 2147483647 and grid[nr][nc] not in visited:
                    visited.add((nr,nc))
                    grid[nr][nc] = grid[r][c]+1
                    q.append([nr,nc])
