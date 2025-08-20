# https://leetcode.com/problems/maximum-average-subarray-i/
class Solution(object):
    def findMaxAverage(self, nums, k):
        n=len(nums)
        current_ele=0
        window_sum=sum(nums[:k])
        max_sum=window_sum
        for i in range(n-k):
            window_sum=window_sum-nums[i]+nums[i+k]
            if window_sum>max_sum:
                max_sum=window_sum
        average=max_sum/float(k)
        return average

 
        