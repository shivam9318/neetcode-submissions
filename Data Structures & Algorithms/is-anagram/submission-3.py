class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        
        # Loop through each character in t
        for char in t:
            if char in s_list:
                s_list.remove(char)   # remove this character
            else:
                return False          # found a mismatch
        
        # After the loop: how do we know if anagram?
        return s_list == [] 









# tat -> if i reverse tat it will be tat same characters
# twit ->. reverse of twit is tiwt not exact same occurence of chars so not anagram