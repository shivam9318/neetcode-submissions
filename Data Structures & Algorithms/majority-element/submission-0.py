class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)/2
        occ = {}
        result = 0
        for i in range(len(nums)):
            occ[nums[i]] = occ.get(nums[i],0) + 1
        for i in occ:
            if occ[i] > majority:
                result = i
                break
        return result