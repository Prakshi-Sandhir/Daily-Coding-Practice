# https://leetcode.com/problems/power-of-two/
class Solution(object):
    def isPowerOfTwo(self, n):
        i = 2
        def poweroftwo(n,i):
            if i>n:
                return False
            i=i*2
            if n==i:
                return True
            return poweroftwo(n,i)
        
        if n==1 or n==2:
            return True
        ans = poweroftwo(n,i)
        return ans
        
        
        