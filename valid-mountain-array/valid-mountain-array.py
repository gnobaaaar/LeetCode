class Solution(object):
    def validMountainArray(self, arr):
        max_index = arr.index(max(arr))
        
        if max_index == 0:
            return 0
        if max_index == len(arr)-1:
            return 0
        
        for i in range(0,max_index):
            if arr[i] >= arr[i+1]:
                return 0
        
        for j in range(max_index,len(arr)-1):
            if arr[j] <= arr[j+1]:
                return 0
        
        return 1