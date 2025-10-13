class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def findFirst(nums, target):
            low, high = 0, n - 1
            first = -1
            while low <= high:
                mid = (low + high) // 2
                if target == nums[mid]:
                    first = mid
                    high = mid - 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return first
        
        def findLast(nums, target):
            low, high = 0, n - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if target == nums[mid]:
                    last = mid
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return last
        
        return [findFirst(nums, target), findLast(nums, target)]