class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR = {}
        countM = {}
        for i in range(len(ransomNote)):
            countR[ransomNote[i]] = countR.get(ransomNote[i],0) + 1
        for i in range(len(magazine)):
            countM[magazine[i]] = countM.get(magazine[i],0) + 1
        for letter,neededcount in countR.items():
            if countM.get(letter,0) < neededcount:
                return False
        return True
        
        