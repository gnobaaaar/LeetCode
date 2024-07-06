class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = tmp * tmp
        nums.sort()
        return(nums)
            