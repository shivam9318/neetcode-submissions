class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closer_to_opener = {"]":"[","}":"{",")":"("}
        for c in s:
            if c in closer_to_opener:
                if not stack:
                    return False
                top = stack.pop()
                if top != closer_to_opener[c]:
                    return False
            else:
                stack.append(c)
        return not stack      

        stack = ["["]
        top = "[", 