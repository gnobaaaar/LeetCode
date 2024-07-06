class Solution(object):
    def findNumbers(self, nums):
        index=0
        for i in nums:
            if len(str(i)) % 2 ==0:
                index += 1
        return(index)
                
        