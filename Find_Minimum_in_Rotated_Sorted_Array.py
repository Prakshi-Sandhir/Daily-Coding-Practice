# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution(object):
    def findMin(self, nums):
        tem=len(nums)
        count,num=nums[0],nums[0]
        st,lst=0,tem-1
        while st<=lst:
            mid=(st+lst)//2
            if nums[mid]>=nums[st]:
                count = min(count, nums[st])
                st=mid+1
            else:
                num = min(num, nums[mid])
                lst=mid-1
      
        if num>count:
            return count
        else:
            return num
 