# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution(object):
    def searchRange(self, nums, target):
        sta, end = -1, -1
        st, lst = 0, len(nums) - 1
        while st <= lst:
            mid = (st + lst) // 2
            if nums[mid] == target:
                sta = mid
                lst = mid - 1
            elif nums[mid] < target:
                st = mid + 1
            else:
                lst = mid - 1

        st, lst = 0, len(nums) - 1
        while st <= lst:
            mid = (st + lst) // 2
            if nums[mid] == target:
                end = mid
                st = mid + 1
            elif nums[mid] < target:
                st = mid + 1
            else:
                lst = mid - 1

        return [sta, end]

