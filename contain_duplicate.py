# https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        j=0
        nums.sort()
        num=len(nums)
        for i in range(num-1):
            if nums[j]==nums[i+1]:
                count=count+1 
                i=i+1
            j=j+1
        if count==0:
            return False
        else:
            return True
        