class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sum = 0
        while n!=1 and n not in seen:
            n = str(n)
            seen.add(int(n))
            for char in n:
                digit = int(char)
                sum = sum + (digit ** 2)
            n = sum
            sum = 0
        return n == 1

