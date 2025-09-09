# https://www.geeksforgeeks.org/problems/second-largest3735/1
class Solution:
    def getSecondLargest(self, arr):
        lar=arr[0]
        mini =-1
        for i in range(len(arr)-1):
            if lar<arr[i+1]:
                mini=lar
                lar=arr[i+1]
            elif arr[i+1]<lar and arr[i+1]>mini:
                mini =arr[i+1]
                
        return mini 
                