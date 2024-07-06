class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        index = 0
        result = 0
        
        for i in nums:
            if i == 1:
                index += 1
                if index > result:
                    result = index
            else:
                index =0
        return result
        