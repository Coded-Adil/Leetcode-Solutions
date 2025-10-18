class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0

        while left <= right:
            width = right - left
            min_height = min(height[left], height[right])
            area = min_height * width

            maxarea = max(maxarea, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxarea