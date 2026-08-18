class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()         # Step 1: create an empty container to store numbers
        for num in nums:    # Step 2: go through each number
            if num in seen:         # Step 3: check if this number is already in 'seen'
                return True  # Step 4: if yes, we found a duplicate
            seen.add(num)   # Step 5: otherwise, store this number
        return False