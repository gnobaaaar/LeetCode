class Solution(object):
    def dominantIndex(self, nums):
        max = nums[0]
        index = 0
        for i in range(len(nums)):
            if max < nums[i]:
                max=nums[i]
                index = i
                
        nums.sort(reverse=True)
        print(nums)
        if nums[0] >= 2* nums[1]:
            return index
        else:
            return -1
                