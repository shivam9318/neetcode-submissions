class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i],0) + 1
        for i,x in enumerate(s):
            if seen[x] == 1:
                return i
        return -1