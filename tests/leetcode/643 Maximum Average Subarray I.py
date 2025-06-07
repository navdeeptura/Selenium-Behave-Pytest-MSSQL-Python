from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k
        max_avg = None
        while j < len(nums) + 1:
            curr_avg: float = sum(nums[i:j]) / k
            if max_avg is None:
                max_avg = curr_avg
            else:
                max_avg = max(max_avg, curr_avg)
            i += 1
            j += 1
        return max_avg

s = Solution()
a = s.findMaxAverage([-1], 1)
print(a)
