# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution(object):
    def searchRange(self, nums, target):
        tem=len(nums)
        sta,end=-1,-1
        st,lst=0,tem-1
        while st<=lst:
            mid=(st+lst)//2
            if nums[mid]==target:
                    sta=mid
            elif nums[mid]>=target:
                lst=mid-1
            else:
                st=mid+1
        while st <= lst:
            mid = (lst+ st) // 2
            if nums[mid] <= target:
                st = mid + 1
            else:
                lst = mid - 1
            if nums[mid] == target:
                last = mid
        return sta,end
