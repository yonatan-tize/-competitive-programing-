class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s = num[0]
        ans = 0
        a = ''
        for i in range(1,len(num)):
            if num[i] == num[i-1]:
                s += num[i]
                if len(s) == 3:
                    if int(s) >= ans:
                        ans = int(s)
                        a = s
            else:
                s = num[i]
        return a

