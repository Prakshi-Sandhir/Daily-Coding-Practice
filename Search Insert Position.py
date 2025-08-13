# https://leetcode.com/problems/search-insert-position/
class Solution(object):
    def searchInsert(self, arr, target):
        tem=len(arr)
        pos=0
        st,lst=0,tem-1
        while st<=lst:
            mid=(st+lst)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                pos=mid
                lst=mid-1

            else:
                pos=mid+1
                st=mid+1
        return pos
        
