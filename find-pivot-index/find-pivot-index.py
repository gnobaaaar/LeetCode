class Solution(object):
    def pivotIndex(self, nums):
        pivot = 0
        left = 0
        right = 0
        
        for i in range(len(nums)):
            if pivot == 0:
                left = 0
            
            left = sum(nums[0:i])
            right = sum(nums[i+1:len(nums)])

            if left == right:
                break
            else:
                pivot +=1
            
        if pivot < len(nums):
            return pivot
        else:
            return -1