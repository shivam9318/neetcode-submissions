class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
            seen = {}
            store = []
            for i in range(len(nums)):
                seen[nums[i]] = seen.get(nums[i],0) + 1
            items = list(seen.items())
            
            def sortedd(pair):
                return(pair[1])
                
            sorted_items = sorted(items, key=sortedd, reverse=True)

            top_k = sorted_items[:k]

            for i in top_k:
                store.append(i[0])
            
            return store