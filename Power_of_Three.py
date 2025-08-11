# https://leetcode.com/problems/power-of-three/
class Solution(object):
    def isPowerOfThree(self, n):
        i=3
        def powerofThree(n,i):
            if i>n:
                return False
            i=i*3
            if n==i:
                return True
            return powerofThree(n,i)
        
        if n==1 or n==3:
            return True
        ans = powerofThree(n,i)
        return ans
        
        
        