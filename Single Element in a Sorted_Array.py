# https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution(object):
    def singleNonDuplicate(self, nums):
        tem = len(nums)
        st, lst = 0, tem - 1
        count = 0
        while st <= lst:
            mid = (st + lst) // 2
            if (mid == 0 or nums[mid] != nums[mid - 1]) and (mid == tem - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    st = mid + 2
                else:
                    lst = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    st = mid + 1
                else:
                    lst = mid - 1

        return -1
      
