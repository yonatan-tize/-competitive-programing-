class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 =[0] * 26
        ls2 = [0] * 26

        for i in s1:
            ls1[ord(i)-ord('a')] += 1 
        
        i1 = 0
        i2 = len(s1)

        for j in s2[:i2]:
            ls2[ord(j)-ord('a')] += 1  

        for k in range(i2, len(s2)+1):
            if ls1 == ls2:
                return True
            if k == len(s2):
                break
            ls2[ord(s2[i1])-ord('a')] -= 1
            ls2[ord(s2[k])-ord('a')] += 1
            i1 += 1
        
        return False

