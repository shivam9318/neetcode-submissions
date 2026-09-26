class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char for char in s if char.isalnum()).lower()
        cleaned_text_rev = cleaned_text[::-1]
        if cleaned_text == cleaned_text_rev:
            return True
        else:
            return False
        