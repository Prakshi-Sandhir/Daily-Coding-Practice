# https://www.geeksforgeeks.org/problems/count-the-zeros2550/0

class Solution:
    
    def countZeroes(self, arr):
        count=0
        j=len(arr)
        for i in range(j):
            if arr[i]>-1 and arr[i]<1:
                count+=1
        return count