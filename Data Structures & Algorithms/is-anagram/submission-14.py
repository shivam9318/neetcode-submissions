class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        seen1 = {}
        seen2 = {}
        for i in range(len(s)):
            seen1[s[i]] = seen1.get(s[i],0) + 1
        for i in range(len(t)):
            seen2[t[i]] = seen2.get(t[i],0) + 1
        
        return seen1 == seen2