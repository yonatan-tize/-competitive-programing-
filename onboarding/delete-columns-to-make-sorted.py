class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            for j in range(1,len(strs)): 
                if ord(strs[j][i]) < ord(strs[j-1][i]):
                    count += 1
                    break
        return count