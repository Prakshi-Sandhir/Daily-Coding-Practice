# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
class Solution:
    def findFloor(self, arr, x):
        tem=len(arr)
        lis=[]
        st=0
        lst=tem-1
        while st<=lst:
            mid=(st+lst)//2
            if arr[mid] <= x:
                 lis.append(mid)
                 st=mid+1
                 
            elif arr[mid]> x:
                # lis.append(mid)
                lst=mid-1
        # print(lis)
        if len(lis)==0:
            return -1
        return lis[-1]
             
                
                
                
        