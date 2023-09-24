from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        for i in range(0,len(nums)-1):
            for j in range(i,len(nums)-1):
                for k in range(j,len(nums)-1):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.append([nums[i], nums[j], nums[k]])
        return triplets
S = Solution()
print ( S.threeSum([-1,0,1,2,-1,-4]))