class Solution(object):
    def isPalindrome(self, x):
        arr = list(str(x))
        arr.reverse()
        tmp = "".join(arr)
        
        if str(x) == str(tmp):
            return 1
        else:
            return 0