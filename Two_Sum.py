# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]== target:
        #             return i,j
        array=[]
        for i,val in enumerate(nums):
            array.append([i,val])
        array.sort(key=lambda x:x[1])
        # print(array)
        start=0
        end=len(array)-1
        for i in range(start,end):
            if array[start][1]+array[end][1]==target:
                return array[start][0],array[end][0]
            elif array[start][1]+array[end][1]>target:
                end=end-1
            else:
                start=start+1
            

            


                
        