# https://leetcode.com/problems/power-of-four/
class Solution(object):
    def isPowerOfFour(self, n):
        i = 4
        def powerofFour(n,i):
            if i>n:
                return False
            i=i*4
            if n==i:
                return True
            return powerofFour(n,i)
        
        if n==1 or n==4:
            return True
        ans = powerofFour(n,i)
        return ans
        
        
        
        