class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        seen=set()
        curr_el=0
        
        for i in range(n):

            if nums[i] in seen:
                return True
            seen.add(nums[i])
            
            # if nums[i] not in seen:
            #     seen.add(nums[i])
 
            if i>=k:
                seen.remove(nums[i - k])
        return False


        