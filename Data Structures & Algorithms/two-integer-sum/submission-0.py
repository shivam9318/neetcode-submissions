class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):           # i = index of first number
            for j in range(i+1, len(nums)):  # j = index of second number
                if nums[i] + nums[j] == target:
                    return [i,j]