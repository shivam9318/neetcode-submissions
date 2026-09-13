class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # seen = {}
        # for i in range(len(nums)):
        #     seen[nums[i]] = i
        nums = set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        return False