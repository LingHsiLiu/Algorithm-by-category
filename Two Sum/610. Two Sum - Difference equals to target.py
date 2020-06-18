# two points
# O(n^2)
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        n = len(nums)
        if target < 0:
            target = -target
        j = 0
        for i in range(n):
            if i == j:
                j += 1
            while j < n and nums[j] - nums[i] < target:
                j += 1
            if j < n and nums[j] - nums[i] == target:
                return [nums[i], nums[j]]
