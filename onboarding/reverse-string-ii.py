class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ls = list(s)
        for i in range(0, len(s), 2* k):
            m = i
            j = min(i + k-1, len(s)-1)
            while m < j:
                ls[m], ls[j] = ls[j], ls[m]
                j -= 1
                m += 1   
        return ''.join(ls)