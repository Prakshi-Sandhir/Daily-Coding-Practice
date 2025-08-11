# https://leetcode.com/problems/binary-search/
class Solution(object):
    def search(self, nums, target):
        tem=len(nums)
        start=0
        last=tem-1
        while start<=last:
            mid=(start+last)//2
            if target == nums[mid]:
                return mid
            elif target>nums[mid]:
                start=mid+1
            elif target<nums[mid]:
                last=mid-1
        return -1
        