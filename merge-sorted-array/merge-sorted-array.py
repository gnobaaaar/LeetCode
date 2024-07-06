class Solution(object):
    def merge(self, nums1, m, nums2, n):
        tmp = []
        if len(nums1) > 0:
            for i in range(m):
                tmp.append(nums1[i])
        
        if len(nums2) > 0:
            for i in range(n):
                tmp.append(nums2[i])
                
        tmp.sort()
        
        for i in range(m+n):
            nums1[i] = tmp[i]