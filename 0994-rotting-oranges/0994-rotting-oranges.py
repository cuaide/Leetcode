class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rs,cs = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rs):
            for c in range(cs):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        time = 0
        dirs = ((1,0), (-1,0), (0,1), (0,-1))

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rs and 0 <= nc < cs and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 
                        fresh -= 1
                        queue.append((nr, nc))
            time += 1

        return time if fresh == 0 else -1