import logging
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return []
        if self.check_sorted(nums):
            print(f"List is Sorted, Target: {target}")
            return self.sorted_array(nums, target)
        else:
            print(f"List is not Sorted, Target: {target}")
            return self.unsorted_array(nums, target)

    def check_sorted(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True

    def sorted_array(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left, right]
            elif current_sum > target:
                right -= 1
            else:
                left += 1
        return []

    def unsorted_array(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict and dict[complement] != i:
                return [dict[complement], i]
            dict[nums[i]] = i
        return []

def test1_check_two_sums():
    test_instance = Solution()
    print ("Output is", test_instance.twoSum([2,7,11,15], 9))
    assert (test_instance.twoSum([2,7,11,15], 9) == [0, 1])
    assert (test_instance.twoSum([3,2,4], 6) == [1, 2])
    assert (test_instance.twoSum([3,3], 6) == [0, 1])
    # Edge case: Empty list
    assert (test_instance.twoSum([], 5) == [])

    # Edge case: Single element list
    assert (test_instance.twoSum([5], 5) == [])

    # Edge case: No valid pair exists
    assert (test_instance.twoSum([1, 2, 3], 10) == [])

    # Edge case: Negative numbers
    assert (test_instance.twoSum([-3, 4, 3, 90], 0) == [0, 2])

    # Edge case: Duplicate values used in different positions
    assert (test_instance.twoSum([1, 5, 1, 5], 10) == [1, 3])

    # Edge case: Large input
    nums = list(range(1, 1000000))  # 1 to 999999
    nums.append(1000001)
    assert (test_instance.twoSum(nums, 1000002) == [0, len(nums) - 1])




"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""