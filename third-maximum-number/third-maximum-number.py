class Solution(object):
    def thirdMax(self, nums):
        result = set(nums)
        arr = sorted(result, reverse=True)
        
        if len(arr) < 3:
            return arr[0]
        else:
            return arr[2]