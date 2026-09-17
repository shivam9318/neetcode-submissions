class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        sorted_list = sorted(nums,reverse=True)
        return(sorted_list[k-1])
        