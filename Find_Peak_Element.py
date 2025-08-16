# https://leetcode.com/problems/find-peak-element/
class Solution(object):
    def findPeakElement(self, nums):
        st, lst = 0, len(nums) - 1
        while st < lst:
            mid = (st + lst) // 2
            if nums[mid] < nums[mid + 1]:
                st = mid + 1
            else:
                lst = mid
        return st
