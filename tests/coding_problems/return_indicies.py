
def twoSums(nums, target):
    index_of_nums = []
    list_1 = []
    for i in range(len(nums)):
        remainder = target - nums[i]

        if remainder in nums:
            list_1.append((i, nums.index(remainder)))
    return list_1



print (twoSums([2, 7, 11, 15], 22))