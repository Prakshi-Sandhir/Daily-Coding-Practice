# https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        i=0
        nums.sort()
        num=len(nums)
        while i< num-1:
            if nums[i]==nums[i+1]:
                i+=2
            else:
                return nums[i]
        return nums[-1]
                
               


        