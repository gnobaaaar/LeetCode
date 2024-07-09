class Solution(object):
    def plusOne(self, digits):
        
        number_str=''.join(map(str, digits))
        numbers=int(number_str)+1
        
        return list(map(int,str(numbers)))
        