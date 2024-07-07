class Solution(object):
    def moveZeroes(self, arr):
        i = 0
        for j in range(i+1, len(arr)):
            if arr[i] == 0 and arr[j] !=0:
                arr[i] = arr[j]
                arr[j] = 0
                i+=1
            elif arr[i] == 0 and arr[j] == 0:
                pass
            else:
                i+=1
