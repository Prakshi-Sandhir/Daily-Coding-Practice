# https://leetcode.com/problems/sort-colors/
class Solution(object):
    def sortColors(self, nums):
        zero,one,two=0,0,0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            elif nums[i]==1:
                one+=1
            else:
                two+=1
        for i in range(zero):
            nums[i]=0
        for i in range(zero,zero+one):
            nums[i]=1
        for i in range(zero+one,len(nums)):
            nums[i]=2
    

        