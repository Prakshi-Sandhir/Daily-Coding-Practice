class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L_val=[1]*len(nums)
        R_val=[1]*len(nums)
        val=[1]*len(nums)
        curr=1
        for i in range (len(nums)):
            R_val[i]=curr
            curr=curr*nums[i]
        curr=1
        for i in range (len(nums)-1,-1,-1):
            L_val[i]=curr
            curr=curr*nums[i]
        for i in range(len(nums)): 
            val[i]=R_val[i]*L_val[i]
        return val



        
        