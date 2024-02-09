class Solution:
    def numberOfWays(self, s: str) -> int:
        #lets find left total
        left = []
        ones = 0
        zeros = 0

        for i in range(len(s)):
            if s[i] == '1':
                left.append(zeros)
                ones += 1
            else:
                left.append(ones)
                zeros += 1

        right = []
        for j in range(len(s)):
            if s[j] == '1':
                right.append(zeros)
                ones -= 1
            else:
                right.append(ones)
                zeros -= 1

        count = 0

        for k in range(len(s)):
            count += left[k] * right[k]

        return count

        

