class Solution(object):
    def removeElement(self, nums, val):
        val_count = 0
        for i in nums:
            if val == i:
                val_count +=1
        
        for i in range(val_count):
            nums.remove(val)