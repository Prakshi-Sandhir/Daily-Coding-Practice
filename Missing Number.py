# https://leetcode.com/problems/missing-number/
class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        current_sum=0
        # for i in range(n+1):
        #     if i not in nums:
        #         return i
        expected_sum=n*(n+1)//2
        for i in range(n):
            current_sum+=nums[i]
        return expected_sum- current_sum
            