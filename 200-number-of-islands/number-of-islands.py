class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        def get_neighbors(coord):
            res = []
            row, col = coord
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < num_rows and 0 <= c < num_cols:
                    res.append((r, c))
            return res
        
        def dfs(coord):
            r, c = coord
            if grid[r][c] != '1':
                return
            grid[r][c] = '0' 
            for neighbor in get_neighbors(coord):
                dfs(neighbor)
        
        count = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '1':
                    dfs((r, c))
                    count += 1
        return count