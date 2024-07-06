class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False
        
        left = 0
        right = len(arr) - 1
        
        while left + 1 < len(arr) and arr[left] < arr[left + 1]:
            left += 1
        
        while right - 1 >= 0 and arr[right] < arr[right - 1]:
            right -= 1
        
        return left == right and left != 0 and right != len(arr) - 1