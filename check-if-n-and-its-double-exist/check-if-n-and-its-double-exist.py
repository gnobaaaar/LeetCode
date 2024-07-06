class Solution(object):
    def checkIfExist(self, arr):
        for i in range(0,len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[j] == 2* arr[i]:
                    return 1
        return 0