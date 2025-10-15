class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num_rows, num_cols = len(image), len(image[0])
        def get_neighbors(coord, colorx):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    if image[neighbor_row][neighbor_col] == colorx:
                        yield neighbor_row, neighbor_col
        
        def bfs(root):
            queue = deque([root])
            visited = [[False for sc in range(num_cols)] for sr in range(num_rows)]
            sr, sc = root
            colorx = image[sr][sc]
            image[sr][sc] = color
            visited[sr][sc] = True
            while len(queue) > 0:
                node = queue.popleft()
                for neighbor in get_neighbors(node, colorx):
                    sr, sc = neighbor
                    if visited[sr][sc]:
                        continue
                    image[sr][sc] = color
                    queue.append(neighbor)
                    visited[sr][sc] = True

        bfs((sr, sc))
        return image