class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k <= 0 or n == 0 or k > n:
            return 0 

        window_sum = 0
        max_sum_with_distinct_elements = 0 
        freq_map = defaultdict(int) 
        distinct_count = 0 

        for i in range(k):
            num = nums[i]
            window_sum += num
            freq_map[num] += 1
            if freq_map[num] == 1:
                distinct_count += 1
        
        if distinct_count == k:
            max_sum_with_distinct_elements = window_sum

        for right in range(k, n):
            left_num = nums[right - k]
            window_sum -= left_num
            freq_map[left_num] -= 1
            if freq_map[left_num] == 0: 
                distinct_count -= 1
            
            right_num = nums[right]
            window_sum += right_num
            freq_map[right_num] += 1
            if freq_map[right_num] == 1:
                distinct_count += 1
            if distinct_count == k:
                max_sum_with_distinct_elements = max(max_sum_with_distinct_elements, window_sum)
            
        return max_sum_with_distinct_elements