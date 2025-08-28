# https://leetcode.com/problems/merge-sorted-array/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        end=len(nums1)-1
        m,n=m-1,n-1
        while m>=0 and n>=0:
            if nums1[m]<=nums2[n]:
                nums1[end]=nums2[n]
                end=end-1
                n=n-1
            elif nums1[m]>nums2[n]:
                nums1[end]=nums1[m]
                # nums1[m]=nums2[n]
                end=end-1
                m=m-1
        while n>=0:
            nums1[end] = nums2[n]
            end-=1
            n-=1
        return nums1


            


        
