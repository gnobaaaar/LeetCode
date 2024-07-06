class Solution(object):
    def duplicateZeros(self, arr):
        tmp = []
        for i in range(len(arr)):
            if arr[i] == 0:
                tmp.append(arr[i])
            tmp.append(arr[i])
        
        answer = tmp[:len(arr)]
        
        for i in range(len(arr)):
            arr[i] = answer[i]