# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
class Solution:
    def maximumSumSubarray (self,arr,k):
        n=len(arr)
        # current_element
        # last_element=k-1
        window_sum=sum(arr[:k])
        max_sum=window_sum
        for i in range(n-k):
            window_sum=window_sum-arr[i]+arr[i+k]
            if max_sum<window_sum:
                max_sum=window_sum
        return max_sum
        