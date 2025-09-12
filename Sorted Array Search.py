#User function Template for python3
# https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1
class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        count=0
        for i in range(len(arr)):
            if arr[i]==k:
                count+=1
                break
            elif arr[i]!=k:
                continue
        if count==0:
            return False
        else:
            return True