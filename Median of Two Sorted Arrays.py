class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=nums1 + nums2
        arr.sort()
        lenn=len(arr)
        l,r=0,lenn-1

        mid=(l+r)//2
        if lenn%2!=0:
            return arr[mid]
        else:
            return (arr[mid]+arr[mid+1])/2


                


        