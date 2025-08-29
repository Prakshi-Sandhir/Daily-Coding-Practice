# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        # for i in range(1,n+1):
        #     m=isBadVersion(i)
        #     if m==True:
            #  return i
        ans=0
        st,lst=1,n
        while st<=lst:
            mid=(st+lst)//2
            m=isBadVersion(mid)
            if m==True:
                ans=mid
                lst=mid-1
            else:
                st=mid+1
        return ans

                 


        