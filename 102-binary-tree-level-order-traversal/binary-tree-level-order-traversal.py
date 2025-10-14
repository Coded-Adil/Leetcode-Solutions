from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Handle empty tree case
        if not root:
            return []
        
        res = []
        queue = deque([root])
        while queue:
            n = len(queue)
            new_level = []
            for _ in range(n):
                node = queue.popleft()
                new_level.append(node.val)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
            res.append(new_level)
        return res