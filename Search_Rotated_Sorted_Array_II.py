# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution(object):
    def search(self, nums, target):
        tem=len(nums)
        st,lst=0,tem-1
        while st<=lst:
            mid=(st+lst)//2
            if nums[mid]==target:
                return True

            if nums[mid]==nums[st] and nums[mid]==nums[lst]:
                st=st+1
                lst=lst-1
                continue
            elif nums[mid]>=nums[st]:
                if nums[mid]>=target and nums[st]<=target:
                    lst=mid-1
                else:
                    st=mid+1
            else:
                if nums[mid]<=target and nums[lst]>=target:
                    st=mid+1
                else:
                    lst=mid-1
        return False









        
        