class Solution(object):
    def twoSum(self, nums, target):
        k = {}
        for c, num in enumerate(nums):
            if target - num in k:
                return k[target-num], c
            k[num] = c


            
        
        