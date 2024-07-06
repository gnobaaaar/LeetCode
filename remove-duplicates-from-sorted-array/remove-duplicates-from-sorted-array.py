class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        fast = 1
        
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        
        return slow + 1