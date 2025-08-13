# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, arr, target):
        tem=len(arr)
        st,lst=0,tem-1
        while st<=lst:
            mid=(st+lst)//2
            if arr[mid]==target:
                return mid
            elif arr[st]<=arr[mid]:
                if arr[st]<=target and arr[mid]>=target:
                    lst=mid-1
                else:
                    st=mid+1
            else:
                if arr[mid]<=target and arr[lst]>=target:
                    st=mid+1
                else:
                    lst=mid
        return -1